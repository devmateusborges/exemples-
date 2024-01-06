from app.generics.generic_type import generic_type


class TypeTstTipoTest1(generic_type):
    TYPE_10 = "10"
    TYPE_11 = "11"
    TYPE_12 = "12"
    TYPE_13 = "13"

    choices = (
        (TYPE_10, "Tipo 10"),
        (TYPE_11, "Tipo 11"),
        (TYPE_12, "Tipo 12"),
        (TYPE_13, "Tipo 13"),
    )


class TypeTst1Radio(generic_type):
    TYPE_OPT1 = "OPT1"
    TYPE_OPT2 = "OPT2"

    choices = (
        (TYPE_OPT1, "Option 1"),
        (TYPE_OPT2, "Option 2"),
    )
