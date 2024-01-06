<?php

class SystemChangeLog extends TRecord
{
    const TABLENAME    = 'system_change_log';
    const PRIMARYKEY   = 'id';
    const IDPOLICY     = 'max';

    public static function register($activeRecord, $lastState, $currentState)
    {
        $table = $activeRecord->getEntity();
        $pk    = $activeRecord->getPrimaryKey();

        if ((strtoupper($table) !==  strtoupper('SYSTEM_CHANGE_LOG')) AND (strtoupper($table) !== strtoupper('SYSTEM_SQL_LOG') ) )  {
            TTransaction::open(TSession::getValue('pConn'));

            if (isset($lastState)) {
                foreach ($lastState as $key => $value) {
                    if (!isset($currentState[$key])) {
                        // deleted
                        $log = new self;
                        $log->tablename  = $table;
                        $log->logdate    = date('Y-m-d H:i:s');
                        $log->login      = TSession::getValue('login');
                        $log->primarykey = $pk;
                        $log->pkvalue    = $activeRecord->$pk;
                        $log->operation  = 'deleted';
                        $log->columnname = $key;
                        $log->oldvalue   = (string) $value;
                        $log->newvalue   = '';
                        $log->unit_id    = TSession::getValue('userunitid');
                        $log->store();
                    }
                }
            }

            foreach ($currentState as $key => $value) {
                if (isset($lastState[$key]) and ($value != $lastState[$key])) {
                    // changed
                    $log = new self;
                    $log->tablename  = $table;
                    $log->logdate    = date('Y-m-d H:i:s');
                    $log->login      = TSession::getValue('login');
                    $log->primarykey = $pk;
                    $log->pkvalue    = $activeRecord->$pk;
                    $log->operation  = 'changed';
                    $log->columnname = $key;
                    $log->oldvalue   = (string) $lastState[$key];
                    $log->newvalue   = (string) is_scalar($value) ? $value : serialize($value);
                    $log->unit_id    = TSession::getValue('userunitid');
                    $log->store();
                }
                if (!isset($lastState[$key]) and !empty($value)) {
                    // created
                    $log = new self;
                    $log->tablename  = $table;
                    $log->logdate    = date('Y-m-d H:i:s');
                    $log->login      = TSession::getValue('login');
                    $log->primarykey = $pk;
                    $log->pkvalue    = $activeRecord->$pk;
                    $log->operation  = 'created';
                    $log->columnname = $key;
                    $log->oldvalue   = '';
                    $log->newvalue   = (string) is_scalar($value) ? $value : serialize($value);
                    $log->unit_id    = TSession::getValue('userunitid');
                    $log->store();
                }
            }

            TTransaction::close();
        }
    }
}
