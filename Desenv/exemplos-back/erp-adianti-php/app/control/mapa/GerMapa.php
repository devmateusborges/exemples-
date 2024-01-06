<?php

use Google\Gmaps;

class GerMapa extends TPage
{

  
    public function __construct($param)
    {
        
       parent::__construct();
       
       $this->div  = new TElement('div');
       $this->div->{'id'} = 'MapMenuLateral';
       $this->form = new BootstrapFormBuilder('Form_Filtro_Map');
       // define the form title
       $this->form->setFormTitle('Listagem de tipo produtos');
  
       $edfiltro_dispositivo = new TDBCombo('edfiltro_dispositivo', 'abdadosdev', 'BorDispositivo', 'id', '{nome}','id asc'  );
       $edfiltro_dt_mov_ini = new TDate('edfiltro_dt_mov_ini');
       $edfiltro_dt_mov_fin = new TDate('edfiltro_dt_mov_fin');

       $edfiltro_dt_mov_ini->setMask('dd/mm/yyyy');
       $edfiltro_dt_mov_fin->setMask('dd/mm/yyyy');       
       
       $edfiltro_dispositivo->setSize('150');
       $edfiltro_dt_mov_ini->setSize('150');
       $edfiltro_dt_mov_fin->setSize('150');
       
       $row1 = $this->form->addFields([new TLabel('Dispositivo')],[$edfiltro_dispositivo]);
       $row2 = $this->form->addFields([new TLabel('Data Inicial')],[$edfiltro_dt_mov_ini],[new TLabel('Data Final')],[$edfiltro_dt_mov_fin]);
       
       //row1->{'class'} = 'xxx';

       $this->form->setData( TSession::getValue(__CLASS__.'_filter_data') );
       
       $this->form->addAction('Buscar', new TAction([$this, 'onReload']), 'fa:search')->addStyleClass('btn-primary');
        
       $container = new TVBox;
       $container->style = 'width: 100%';
       

       $this->div->add($this->form);
      

       $panel = new TPanelGroup;
       $panel->add($this->loadMap($param));
       
       $this->div->add($panel);

       $container->add($this->div);

       parent::add($container);

        
    
    }
  
    public function loadMap($param)
    {

        
        $dtini = '2000-05-03 21:36:41';
        $dtfim = '2050-05-06 21:36:41';
//        $dtini =isset($param['edfiltro_dt_mov_ini']) ? date('Y-m-d',$param['edfiltro_dt_mov_ini']) : '1900-01-01';
  //      $dtfim =isset($param['edfiltro_dt_mov_fin']) ? date('Y-m-d',$param['edfiltro_dt_mov_fin']) : '2500-01-01';
  
        
        $dt=date('YmdHis');
        $linha=1;

        $datas = date('Y-m-d H:i:s', strtotime("-10 days"));
        
        //echo date($datas, strtotime("+1 days"));        
        $lats='-20.58252';
        $longs='-47.86284';
        $cont=0;
        $sql="";


        $data = $this->form->getData();
        
        TTransaction::open('abdadosdev');
        $conection =  TTransaction::get();
        $queryPrep = $conection->prepare("select gps_lat as lat, gps_long as lng from bor_mov where dthr_track between '$dtini' and '$dtfim'");
        $queryPrep->execute();
        $result = $queryPrep->fetchAll();
        $objeto=[];
        $tt=100;
        $poly = '';
        /*foreach($result as $row=>$value)
        {
 
            $objeto[$row]['Maker_Id']='mk124';
            $objeto[$row]['Maker_Title']='mk titulo';
            $objeto[$row]['Maker_Lat']= substr($result[$row]['gps_lat'], 0, 5) . $tt ;
            $objeto[$row]['Maker_Lng']=$result[$row]['gps_long'];
            $objeto[$row]['Maker_InfoWindow']='<h2>mk teste</h2>';
            $objeto[$row]['Maker_Problem']= $row===0 ? 'R' : 'G';  
            $poly = $poly . $result[$row]['gps_long'] . ',' . substr($result[$row]['gps_lat'], 0, 5) . $tt . ';';
            $tt=$tt + 300;
            
        }*/

        $json = json_encode( $result );

        $this->output = $json ;
        (string)$arquivo = 'app/output/mapa/js/pontos.json';
        file_put_contents($arquivo,  $this->output);        

        //echo $json;

        TTransaction::close();        

        $gmconfig['ContextUrl']='agrobot/erp';
        $gmconfig['divName']='x1';
        $gmconfig['divHeight']='800';
        $gmconfig['divUOMWidth']='px';
        $gmconfig['divWidth']='100';
        $gmconfig['divUOMWidth']='%';
        $gmconfig['zoom']='15';
        $gmconfig['CenterLatLng']='-20.58252,-47.86284';
        $gmconfig['mapType']='SATELLITE';
        $gmconfig['overviewMapControl']=false;
        $gmconfig['mapMaker']=false;
        $gmconfig['mapTypeControl']=false;
                    

        $gm = new Gmaps($gmconfig);

    
        $gm->GmapsMakers = $objeto;
        
        $gm->GmapsPolylines = [
            ['Polyline_Id'=> 'sdfs',
             'Polyline_Paths'=> substr($poly, 0, -1), // '-47.86284,-20.58100;-47.86284,-20.58400;-47.86284,-20.58700',
             'Polyline_StrokeColor'=>'#FF0000',
             'Polyline_StrokeOpacity'=> 1.0 ,
             'Polyline_StrokeWeight'=> 4 ,
             'Polyline_Geodesic'=>'1']

          ];          


        $arquivo = $gm->exibe_mapa();
    
        $iframe = new TElement('iframe');
        $iframe->id = "iframe_external";
        $iframe->src = ".$arquivo";
        
        $iframe->frameborder = "0";
        $iframe->scrolling = "yes";
        $iframe->width = "100%";
        $iframe->height = "700px";
        
        unset($gm);


        TSession::setValue(get_class($this).'_filter_data', $data);
        $this->form->setData($data);


        return $iframe;
        

    }    
   
    public function onReload($params = null)
    {
        $this->loaded = TRUE;
        $data=null;

        $this->form->setData($data);
    }

}  
?>
