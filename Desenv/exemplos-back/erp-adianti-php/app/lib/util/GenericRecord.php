<?php

class GenericRecord extends TRecord
{
    const LOG_USER  = false;
    const LOG_TAB   = false;

    public function __constructa($id = NULL)
    {
        parent::__construct($id);
    }

    public function onAfterDelete($object)
    {
        $class = get_class($this);
        if (constant("{$class}::LOG_TAB")) {
            SystemChangeLog::register($this, $object, array());
        }
    }
    public function onBeforeStore($object)
    {
        $class = get_class($this);
        $pk = $this->getPrimaryKey();

        $att = (array)parent::getAttributes();
        if (in_array("unit_id", $att) and empty($object->unit_id)) {
            $object->unit_id = TSession::getValue('userunitid');
        }

        if (isset($object->$pk)) {
            $pkval = $object->$pk;

            $this->lastState = array();
            if (isset($object->$pk) and self::exists($object->$pk)) {
                $this->lastState = parent::load($object->$pk)->toArray();
            }

            if (constant("{$class}::LOG_USER")) {


                if (in_array("user_id_i", $att) and empty($pkval)) {
                    $object->cod_usr_ins = TSession::getValue('userid');
                }
                if (in_array("date_i", $att) and empty($pkval)) {
                    $object->dt_ins =  date('Y-m-d H:i:s');
                }
                if (in_array("user_id_u", $att) and !empty($pkval)) {
                    $object->cod_usr_upd = TSession::getValue('userid');
                }
                if (in_array("date_u", $att) and !empty($pkval)) {
                    $object->dt_upd =  date('Y-m-d H:i:s');
                }
            }
        }
        
    }

    public function onAfterStore($object)
    {
        $class = get_class($this);
        if (constant("{$class}::LOG_TAB")) {
            SystemChangeLog::register($this, $this->lastState, (array)$object);
        }
    }

}
