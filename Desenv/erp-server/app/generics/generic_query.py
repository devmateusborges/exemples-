"""
    Example query string:

        {
            "filter" : {
                "or" : {
                    "firstname" : {
                        "equals" : "Jhon"
                    },
                    "lastname" : "Galt",
                    "uid" : {
                        "like" : "111111"
                    }
                },
                "and" : {
                    "status" : "active",
                    "age" : {
                        "gt" : 18
                    }
                }
            },
            "sort" : {
                { "firstname" : "asc" },
                { "age" : "desc" }
            }
        }

"""
from sqlalchemy import and_, or_, desc, asc


def get_generic_query(model, query, session=None, enabled_filter_fields=None):
    """:model: SQLAlchemy model
    :query: valid string filter
    :session: SQLAlchemy session
    :enabled_filter_fields: Fields array allowed for make a query *optional
    """
    # TODO: make session to optional
    instance = GenericQuery(model, query, session, enabled_filter_fields)
    return instance.search()


OPERATORS = {
    "like": lambda f, a: f.ilike(a),
    "equals": lambda f, a: f == a,
    "is_null": lambda f: f is None,
    "is_not_null": lambda f: f is not None,
    "gt": lambda f, a: f > a,
    "gte": lambda f, a: f >= a,
    "lt": lambda f, a: f < a,
    "lte": lambda f, a: f <= a,
    "in": lambda f, a: f.in_(a),
    "not_in": lambda f, a: ~f.in_(a),
    "not_equal_to": lambda f, a: f != a,
}


class GenericQuery(object):
    def __init__(self, model, query, session=None, enabled_filter_fields=None):
        self.model = model
        self.query = query
        if hasattr(model, "query"):
            self.model_query = model.query
        else:
            self.model_query = session.query(self.model)
        self.enabled_filter_fields = enabled_filter_fields

    def search(self):

        result = self.model_query

        filters = self.query
        if filters is not None:
            if "filter" in filters.keys():
                result = self.parse_filter(filters["filter"])
            if "sort" in filters.keys():
                result = result.order_by(*self.sort(filters["sort"]))

        return result

    def parse_filter(self, filters):
        for filter_type in filters:
            if filter_type == "or" or filter_type == "and":
                conditions = []
                for field in filters[filter_type]:
                    if self.is_field_allowed(field):
                        conditions.append(
                            self.create_query(
                                self.parse_field(field, filters[filter_type][field])
                            )
                        )
                if filter_type == "or":
                    self.model_query = self.model_query.filter(or_(*conditions))
                elif filter_type == "and":
                    self.model_query = self.model_query.filter(and_(*conditions))
            else:
                if self.is_field_allowed(filter_type):
                    conditions = self.create_query(
                        self.parse_field(filter_type, filters[filter_type])
                    )
                    self.model_query = self.model_query.filter(conditions)
        return self.model_query

    def parse_field(self, field, field_value):
        if type(field_value) is dict:
            # TODO: check operators and emit error
            operator = list(field_value)[0]
            if self.verify_operator(operator) is False:
                return "Error: operator does not exist", operator
            value = field_value[operator]

            if operator == "like" and (value is None or value == ""):
                value = "%"

        elif type(field_value) is str:
            operator = "equals"
            value = field_value

        return field, operator, value

    @staticmethod
    def verify_operator(operator):
        try:
            if hasattr(OPERATORS[operator], "__call__"):
                return True
            else:
                return False
        except ValueError:
            return False

    def is_field_allowed(self, field):
        if self.enabled_filter_fields:
            return field in self.enabled_filter_fields
        else:
            return True

    def create_query(self, attr):
        field = attr[0]
        operator = attr[1]
        value = attr[2]
        model = self.model

        if "." in field:
            field_items = field.split(".")
            field_name = getattr(model, field_items[0], None)
            class_name = field_name.property.entity.mapper.class_
            new_model = getattr(class_name, field_items[1])
            return field_name.has(OPERATORS[operator](new_model, value))

        return OPERATORS[operator](getattr(model, field, None), value)

    def sort(self, sort_list):
        order = []
        for sort in sort_list:
            if sort_list[sort] == "asc":
                order.append(asc(getattr(self.model, sort, None)))
            elif sort_list[sort] == "desc":
                order.append(desc(getattr(self.model, sort, None)))
        return order
