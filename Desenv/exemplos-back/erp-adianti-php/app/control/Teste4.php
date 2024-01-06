<?php

/*
class TTeste4 extends TPage
{

    public function __construct()
    {

        parent::__construct();

        $this->x = new TDxDataGrid(
            "DxTeste1",
            [
                "pConfig" => TSession::getValue('pConfig'),
                "pSql" => "SELECT cod_categ, desc_categ, to_char(dt_ins, 'rrrr/mm/dd hh24:mi:ss') as dt_ins from tprod_categ where rownum <= 10000",
                "pFieldPK" => "cod_categ",
                "pSelectionMode" => "single",
                "pPageSize" => "10",
                "pColunms" => [
                    "cod_categ" => [
                        "caption" => "Código",
                        "dataType"=> "number",
                        "alignment"=> "center",
                        "allowGrouping"=>"false"
                    ],
                    "desc_categ" => [
                        "caption" => "Descricao",
                        "dataType"=> "string",
                        "alignment"=> "left",
                        "allowGrouping"=>"true"
                    ],
                    "dt_ins" => [
                        "caption" => "Data Inclusão",
                        "dataType"=> "date",
                        "format" => "dd/MM/yyyy hh:mm:ss",
                        "alignment" => "center",
                        "allowGrouping" => "false"
                    ]
                ]
            ]
        );

        parent::add($this->x);
    }
}
?>
*/


class Teste4 extends TPage
{
    public function __construct()
    {
        
        $gmconfig['ContextUrl']='GSBWeb';
        $gmconfig['divName']='x1';
        $gmconfig['divHeight']='800';
        $gmconfig['divUOMWidth']='px';
        $gmconfig['divWidth']='100';
        $gmconfig['divUOMWidth']='%';
        $gmconfig['zoom']='15';
        $gmconfig['CenterLatLng']='-22.603227075277779200,-47.008064148888889600';
        $gmconfig['mapType']='SATELLITE';
        $gmconfig['overviewMapControl']=false;
        $gmconfig['mapMaker']=false;
        $gmconfig['mapTypeControl']=false;
                    

        $gm = new Gmaps($gmconfig);


        $gm->GmapsPolygons = [
            ['Polygon_Id'=>'chave123id',
            'Polygon_Paths'=>'-47.008064148888889600,-22.603227075277779200;-47.008388212222220800,-22.599183617222220800;-47.008590414444441600,-22.599167550555552000;-47.009103311944441600,-22.599509723333331200;-47.009525495000000000,-22.599798065833334400;-47.009893396944441600,-22.600117803888889600;-47.010230627222220800,-22.600443205833337600;-47.010490248333331200,-22.600702928611113600;-47.010560795555558400,-22.600880111944444800;-47.010520607777779200,-22.601115032222224000;-47.010636858333337600,-22.601350620833334400;-47.010837606388889600,-22.601558670000003200;-47.011032304444441600,-22.601706853888889600;-47.011185336944441600,-22.601891048611110400;-47.011358955277779200,-22.602159229444444800;-47.009784808333337600,-22.604485501111113600;-47.008064148888889600,-22.60322707527777920',
            'Polygon_StrokeColor'=>'#fff',
            'Polygon_StrokeOpacity'=>'1',
            'Polygon_StrokeWeight'=>'1',
            'Polygon_FillColor'=>'green',
            'Polygon_FillOpacity'=>'0.7',
            'Polygon_InfoWindow'=>'<h1> teste123 </h1>',
            'Polygon_Draggable'=>'false',
            'Polygon_Editable'=>'false',
            'Polygon_Geodesic'=>'false',
            'Polygon_Title'=>'chave123',
            'Polygon_TitleLatLng'=>'-47.008064148888889600,-22.603227075277779200',
            'Polygon_TitleFontSize'=>'12'],
            ['Polygon_Id'=>'chave124id',
            'Polygon_Paths'=>'-47.008929776388889600,-22.595671330833334400;-47.008819263333337600,-22.595352762222220800;-47.008690565000000000,-22.594712528888886400;-47.008590538888889600,-22.594335296666662400;-47.008416380833331200,-22.594058870833334400;-47.008162420833337600,-22.593933046388886400;-47.007934761388889600,-22.593677484444444800;-47.007733860555552000,-22.593259668888886400;-47.007543201111110400,-22.592798095833331200;-47.007362823611110400,-22.592350187222220800;-47.007177276944448000,-22.591892378333331200;-47.006986893888883200,-22.591428082777779200;-47.006730341944448000,-22.590784986111110400;-47.006871961388889600,-22.590722098055555200;-47.007197789444448000,-22.590751545555555200;-47.007702755833337600,-22.590832557499996800;-47.008033458611110400,-22.590864536388889600;-47.008535446666668800,-22.590901170833334400;-47.009011129444448000,-22.590916679722220800;-47.009338238611116800,-22.590952716944441600;-47.008929776388889600,-22.59567133083333440',
            'Polygon_StrokeColor'=>'#fff',
            'Polygon_StrokeOpacity'=>'1',
            'Polygon_StrokeWeight'=>'1',
            'Polygon_FillColor'=>'red',
            'Polygon_FillOpacity'=>'0.7',
            'Polygon_InfoWindow'=>'<h1> teste124 </h1>',
            'Polygon_Draggable'=>'false',
            'Polygon_Editable'=>'false',
            'Polygon_Geodesic'=>'false',
            'Polygon_Title'=>'chave124',
            'Polygon_TitleLatLng'=>'-47.008929776388889600,-22.595671330833334400',
            'Polygon_TitleFontSize'=>'12']            
        ];

        $gm->GmapsMakers = [
            ['Maker_Id'=>'mk124',
            'Maker_Title'=>'mk titulo',
            'Maker_Lat'=>'-22.595671330833334400',
            'Maker_Lng'=>'-47.008929776388889600',
            'Maker_InfoWindow'=>'<h2>mk teste</h2>',
            'Maker_Problem'=>'R'],
            ['Maker_Id'=>'mk123',
            'Maker_Title'=>'mk titulo',
            'Maker_Lat'=>'-22.603227075277779200',
            'Maker_Lng'=>'-47.008064148888889600',
            'Maker_InfoWindow'=>'<h2>mk teste2</h2>',
            'Maker_Problem'=>'G'],            
        ];
    
        $arquivo = $gm->create_map(true,'Gmaps'.date('YmdHisu'));
    
        $iframe = new TElement('iframe');
        $iframe->id = "iframe_external";
        $iframe->src = ".$arquivo.";
        $iframe->frameborder = "0";
        $iframe->scrolling = "yes";
        $iframe->width = "100%";
        $iframe->height = "700px";
        
        parent::add($iframe);
        
        unset($gm);
        
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $div = new TElement('div');
        $div->add( $this->getBarChart() );
        $div->add( $this->getLineChart() );
        $div->add( $this->getPieChart() );
        $vbox->add($div);
        parent::add($vbox);
       
    
    }
  
    public function getLineChart()
    {
        $html = new THtmlRenderer('app/resources/google_line_chart.html');
        $data = array();
        $data[] = [ 'Day', 'Value 1', 'Value 2', 'Value 3' ];
        $data[] = [ 'Day 1',   120,       140,       160 ];
        $data[] = [ 'Day 2',   100,       120,       140 ];
        $data[] = [ 'Day 3',   140,       160,       180 ];
        # PS: If you use values from database ($row['total'), 
        # cast to float. Ex: (float) $row['total']
        $panel = new TPanelGroup('Line chart');
        $panel->style = 'width: 100%';
        $panel->add($html);
        // replace the main section variables
        $html->enableSection('main', array('data'   => json_encode($data),
                                           'width'  => '100%',
                                           'height'  => '800px',
                                           'title'  => 'Accesses by day',
                                           'ytitle' => 'Accesses', 
                                           'xtitle' => 'Day',
                                           'uniqid' => uniqid()));
        $container = new TElement('div');
        $container->class = 'col-sm-6';
        $container->add($panel);
        return $container;
    }
    public function getBarChart()
    {
        $html = new THtmlRenderer('app/resources/google_bar_chart.html');
        $data = array();
        $data[] = [ 'Day', 'Value 1', 'Value 2', 'Value 3' ];
        $data[] = [ 'Day 1',   100,       120,       140 ];
        $data[] = [ 'Day 2',   120,       140,       160 ];
        $data[] = [ 'Day 3',   140,       160,       180 ];
        # PS: If you use values from database ($row['total'), 
        # cast to float. Ex: (float) $row['total']
        $panel = new TPanelGroup('Bar chart');
        $panel->style = 'width: 100%';
        $panel->add($html);
        // replace the main section variables
        $html->enableSection('main', array('data'   => json_encode($data),
                                           'width'  => '100%',
                                           'height'  => '300px',
                                           'title'  => 'Accesses by day',
                                           'ytitle' => 'Accesses', 
                                           'xtitle' => 'Day',
                                           'uniqid' => uniqid()));
        // add the template to the page
        $container = new TElement('div');
        $container->class = 'col-sm-6';
        $container->add($panel);
        return $container;
    }
    public function getPieChart()
    {
        $html = new THtmlRenderer('app/resources/google_pie_chart.html');
        $data = array();
        $data[] = [ 'Pessoa', 'Value' ];
        $data[] = [ 'Pedro',   40 ];
        $data[] = [ 'Maria',   30 ];
        $data[] = [ 'João',    30 ];
        # PS: If you use values from database ($row['total'), 
        # cast to float. Ex: (float) $row['total']
        $panel = new TPanelGroup('Pie chart');
        $panel->add($html);
        // replace the main section variables
        $html->enableSection('main', array('data'   => json_encode($data),
                                           'width'  => '100%',
                                           'height'  => '300px',
                                           'title'  => 'Accesses by day',
                                           'ytitle' => 'Accesses', 
                                           'xtitle' => 'Day',
                                           'uniqid' => uniqid()));
        $container = new TElement('div');
        $container->class = 'col-sm-6';
        $container->add($panel);
        return $container;
    }


}  
