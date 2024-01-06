<?php

require_once('lib\devexpress\widget\TDxCommun.php');

class TDxDataGrid extends TElement
{
    
    protected $pConfig;
    protected $pSql;
    protected $pFieldPK;
    protected $pSelectionMode;
    protected $pColunms;

    public function __construct($tagname, $pParam)
    {

        //$pTipoSelecao: sigle, multiple

        parent::__construct('div');
        $this->pConfig = $pParam['pConfig'];
        $this->pSql = $pParam['pSql'];
        $this->pFieldPK = $pParam['pFieldPK'];
        $this->pSelectionMode = $pParam['pSelectionMode'];
        $this->pColunms = (array) $pParam['pColunms'];
        $this->pPageSize= $pParam['pPageSize'];
        $this->id = 'tdxdatagrid_' . uniqid();
    }

    public function show()
    {
        TTransaction::open($this->pConfig);
        $conn = TTransaction::get();
        $sth = $conn->prepare($this->pSql);

        $sth->execute();
        $result = $sth->fetchAll(PDO::FETCH_OBJ);

        $ScriptC = '$(document).ready( function() {
            var ds = ' . json_encode($result) . ';
            

            $("#' . $this->id . '" ).dxDataGrid({
                dataSource: ds,
                columnHidingEnabled: true,
                rowAlternationEnabled: true,
                keyExpr: "' . $this->pFieldPK . '",
                selection: {
                    mode: "' . $this->pSelectionMode . '"
                },
                "export": {
                    enabled: true,
                    fileName: "PlanilhaExportada",
                    allowExportSelectedData: true
                },
                showBorders: true,
                filterRow: {
                    visible: true,
                    applyFilter: "auto"
                },
                searchPanel: {
                    visible: true,
                    width: 150,
                    placeholder: "Procurar..."
                },
                headerFilter: {
                    visible: true
                },
                filterPanel: {
                    visible: true
                },
                groupPanel: {
                    visible: true
                },
                columnChooser: {
                    enabled: true,
                    mode: "select"
                },
                pager: {
                    showPageSizeSelector: true,
                    allowedPageSizes: [10, 25, 100, 1000],
                    showInfo: true,
                    showNavigationButtons: true,
                    visible: true
                },
                paging: {
                    pageSize: ' . $this->pPageSize . '
                },
                
                columns: [';

                foreach ($this->pColunms as $key => $value) {
                    
                    $vdataType = TDxCommun::DxProp($value,'dataType',true);
                    $vcaption = TDxCommun::DxProp($value,'caption',true);
                    $valignment = TDxCommun::DxProp($value,'alignment',true);
                    $vformat = TDxCommun::DxProp($value,'center',true);
                    $vallowGrouping = TDxCommun::DxProp($value,'allowGrouping',false);
                    $ScriptC .= '{dataField: "'.$key.'"'.$vdataType.$vcaption.$vformat.$valignment.$vallowGrouping.'},'; 
          
                }

                $ScriptC .= '], 
               
                onSelectionChanged: function (selectedItems) {
                    var data = selectedItems.selectedRowsData[0];
                    if(data) {
                        /*alert(data.' . $this->pFieldPK . ');*/
                        /*location.replace("index.php?class=TProdCategForm&method=onEdit&key=1&cod_categ=1");*/
                    }
                }
            });
                      
            });';
        
        TScript::create($ScriptC);
        parent::show();
        TTransaction::close();
    }


 
}
