<?php
namespace Google;

class Gmaps
{

    protected $output;
    
    //Opções de Inicialização do Mapa
    private $ContextUrl                       = ''; //Nome pasta do httdocs que esta aplicação
    private $divName                          = 'map-canvas';
    private $divWidth                         = 250;
    private $divHeight                        = 250;
    private $divUOMWidth                      = 'px';
    private $divUOMHeight                     = 'px';
    private $zoom                             = 'auto';
    private $backgroundColor                  = null;  //Color used for the background of the Map div
    private $disableDefaultUI                 = true;  //Enables/disables all default UI. May be overridden individually.
    private $disableDoubleClickZoom           = true;  //Enables/disables zoom and center on double click. Enabled by default.
    private $draggable                        = true;  //If false, prevents the map from being dragged. Dragging is enabled by default.
    private $draggableCursor                  = null;  //The name or url of the cursor to display when mousing over a draggable map.
    private $draggingCursor                   = null;  //The name or url of the cursor to display when the map is being dragged.
    private $heading                          = null;  //The heading for aerial imagery in degrees measured clockwise from cardinal direction North. Headings are snapped to the nearest available angle for which imagery is available.
    private $keyboardShortcuts                = true;  //If false, prevents the map from being controlled by the keyboard. Keyboard shortcuts are enabled by default.
    private $mapMaker                         = false; //True if Map Maker tiles should be used instead of regular tiles
    private $mapTypeControl                   = true;  //The initial enabled/disabled state of the Map type control.
    private $maxZoom                          = null;  //The maximum zoom level which will be displayed on the map. If omitted, or set to null, the maximum zoom from the current map type is used instead.
    private $minZoom                          = null;  //The minimum zoom level which will be displayed on the map. If omitted, or set to null, the minimum zoom from the current map type is used instead.
    private $noClear                          = true;  //If true, do not clear the contents of the Map div.
    private $overviewMapControl               = true;  //The enabled/disabled state of the Overview Map control.
    private $panControl                       = true;  //The enabled/disabled state of the Pan control.
    private $rotateControl                    = true;  //The enabled/disabled state of the Rotate control.
    private $scaleControl                     = true;  //The initial enabled/disabled state of the Scale control.
    private $scrollwheel                      = true;  //If false, disables scrollwheel zooming on the map. The scrollwheel is enabled by default.
    private $streetViewControl                = true;  //The initial enabled/disabled state of the Street View Pegman control. This control is part of the default UI, and should be set to false when displaying a map type on which the Street View road overlay should not appear (e.g. a non-Earth map type).
    private $tilt                             = null;  //The angle of incidence of the map as measured in degrees from the viewport plane to the map plane. The only currently supported values are 0, indicating no angle of incidence (no tilt), and 45, indicating a tilt of 45deg;. 45deg; imagery is only available for SATELLITE and HYBRID map types, within some locations, and at some zoom levels.
    private $zoomControl                      = true;  //The enabled/disabled state of the Zoom control.
    private $mapType                          = 'ROADMAP';  //HYBRID; ROADMAP; SATELLITE; TERRAIN
    private $DirectionsTravelMode             = 'DRIVING';  //BICYCLING;DRIVING;TRANSIT;WALKING
    private $CenterLatLng                     = '0';   

    public $GmapsLocations = array();
    //location_address
    //location_title    
    //location_icon     
    //location_content 
    public $GmapsRoutes = array();
    //location_address_start
    //location_address_end
    public $GmapsPolygons = array();
    //Polygon_Id
    //Polygon_Paths
    //Polygon_StrokeColor
    //Polygon_StrokeOpacity
    //Polygon_StrokeWeight
    //Polygon_FillColor
    //Polygon_FillOpacity
    //Polygon_InfoWindow
    //Polygon_DraggAble
    //Polygon_Editable
    //Polygon_Geodesic
    //Polygon_Title
    //Polygon_TitleLatLng
    //Polygon_TitleFontSize
    public $GmapsMakers = array();
    //Maker_Id
    //Maker_Title
    //Maker_Lat
    //Maker_Lng
    //Maker_InfoWindow
    //Maker_Problem
    public $GmapsPolylines = array();
    //PolyLine_Id
    //PolyLine_Paths
    //PolyLine_StrokeColor
    //PolyLine_StrokeOpacity
    //PolyLine_StrokeWeight
    //PolyLine_Geodesic

    public function __construct($config)
    {
        if (count($config) > 0) {
            $this->initialize($config);
        }
    }

    private function initialize($config)
    {
        foreach ($config as $key=>$val) {
            //print_r($key.'=>');
            //print_r($val.'<br>');
            $this->$key = $val;
            
        }
    }
    public function exibe_mapa(){
           

        try {

                    (string)$arquivo = 'app/output/mapa/index.html';
                    //file_put_contents($arquivo,  $this->output);

                    return '/'.$arquivo;
            }
            catch (Exception $e)
            {
                error_log('Erro Gmaps.php - '.$e->getMessage());
            }
    }
    public function create_map($debug,$pMapFileName) {
        
        if($debug) { error_log('Iniciando Criação'); };
        try {
        $this->output .= '
                    <html>
                        <head>
                        <meta charset="UTF-8">
                            <body>
                            <div>
                            <div id="'.$this->divName.'" style="width:'.$this->divWidth.$this->divUOMWidth.';height:'.$this->divHeight.$this->divUOMHeight.'"></div>
                            </div>
                            </body>

                    <script>

                    function initMap() {

                    var d="prototype";function e(a){this.set("fontFamily","Arial");this.set("fontSize",6);this.set("fontColor","#fff");this.set("strokeWeight",0);this.set("strokeColor","#fff");this.set("align","center");this.set("zIndex",1E3);this.setValues(a)}e.prototype=new google.maps.OverlayView;window.MapLabel=e;e[d].changed=function(a){switch(a){case "fontFamily":case "fontSize":case "fontColor":case "strokeWeight":case "strokeColor":case "align":case "text":return h(this);case "maxZoom":case "minZoom":case "position":return this.draw()}};
                    function h(a){var b=a.a;if(b){var f=b.style;f.zIndex=a.get("zIndex");var c=b.getContext("2d");c.clearRect(0,0,b.width,b.height);c.strokeStyle=a.get("strokeColor");c.fillStyle=a.get("fontColor");c.font=a.get("fontSize")+"px "+a.get("fontFamily");var b=Number(a.get("strokeWeight")),g=a.get("text");if(g){if(b)c.lineWidth=b,c.strokeText(g,b,b);c.fillText(g,b,b);a:{c=c.measureText(g).width+b;switch(a.get("align")){case "left":a=0;break a;case "right":a=-c;break a}a=c/-2}f.marginLeft=a+"px";f.marginTop=
                    "-0.4em"}}}e[d].onAdd=function(){var a=this.a=document.createElement("canvas");a.style.position="absolute";var b=a.getContext("2d");b.lineJoin="round";b.textBaseline="top";h(this);(b=this.getPanes())&&b.mapPane.appendChild(a)};e[d].onAdd=e[d].onAdd;
                    e[d].draw=function(){var a=this.getProjection();if(a&&this.a){var b=this.get("position");if(b){b=a.fromLatLngToDivPixel(b);a=this.a.style;a.top=b.y+"px";a.left=b.x+"px";var b=this.get("minZoom"),f=this.get("maxZoom");if(b===void 0&&f===void 0)b="";else{var c=this.getMap();c?(c=c.getZoom(),b=c<b.c>f?"hidden":""):b=""}a.visibility=b}}};e[d].draw=e[d].draw;e[d].onRemove=function(){var a=this.a;a&&a.parentNode&&a.parentNode.removeChild(a)};e[d].onRemove=e[d].onRemove;


                    var initial = new google.maps.LatLng('.explode(',',$this->CenterLatLng)[0].','.explode(',',$this->CenterLatLng)[1].');
                    var mapOptions = {
                    center: initial'.chr(10);
                    if(isset($this->zoom)) {
                        if ($this->zoom=='auto') {
                            $this->output .='       ,zoom: 0'.chr(10);
                        } else {
                            $this->output .='       ,zoom: '.$this->zoom.chr(10);  
                        }
                    }
                    if(isset($this->mapType)) {
                    $this->output .='       ,mapTypeId: google.maps.MapTypeId.'.$this->mapType.chr(10);
                    }
                    if(isset($this->disableDefaultUI)) {
                    $this->output .='       ,disableDefaultUI: '.json_encode($this->disableDefaultUI).chr(10);
                    }
                    if(isset($this->disableDoubleClickZoom)) {
                    $this->output .='       ,disableDoubleClickZoom: '.json_encode($this->disableDoubleClickZoom).chr(10);
                    }
                    if(isset($this->draggable)) {
                    $this->output .='       ,draggable: '.json_encode($this->draggable).chr(10);
                    }
                    if(isset($this->draggableCursor)) {
                    $this->output .='       ,draggableCursor: '.$this->draggableCursor.chr(10);
                    }
                    if(isset($this->draggingCursor)) {
                    $this->output .='       ,draggableCursor: '.$this->draggingCursor.chr(10);
                    }
                    if(isset($this->heading)) {
                    $this->output .='       ,heading: '.$this->heading.chr(10);
                    }
                    if(isset($this->keyboardShortcuts)) {
                    $this->output .='       ,keyboardShortcuts: '.json_encode($this->keyboardShortcuts).chr(10);
                    }
                    if(isset($this->mapMaker)) {
                    $this->output .='       ,mapMaker: '.json_encode($this->mapMaker).chr(10);
                    }
                    if(isset($this->mapTypeControl)) {
                    $this->output .='       ,mapTypeControl: '.json_encode($this->mapTypeControl).chr(10);
                    }
                    if(isset($this->maxZoom)) {
                    $this->output .='       ,maxZoom: '.$this->maxZoom.chr(10);
                    }
                    if(isset($this->minZoom)) {
                    $this->output .='       ,minZoom: '.$this->minZoom.chr(10);
                    }
                    if(isset($this->noClear)) {
                    $this->output .='       ,noClear: '.json_encode($this->noClear).chr(10);
                    }
                    if(isset($this->overviewMapControl)) {
                    $this->output .='       ,overviewMapControl: '.json_encode($this->overviewMapControl).chr(10);
                    }
                    if(isset($this->panControl)) {
                    $this->output .='       ,panControl: '.json_encode($this->panControl).chr(10);
                    }
                    if(isset($this->rotateControl)) {
                    $this->output .='       ,rotateControl: '.json_encode($this->rotateControl).chr(10);
                    }
                    if(isset($this->scaleControl)) {
                    $this->output .='       ,scaleControl: '.json_encode($this->scaleControl).chr(10);
                    }
                    if(isset($this->scrollwheel)) {
                    $this->output .='       ,scrollwheel: '.json_encode($this->scrollwheel).chr(10);
                    }
                    if(isset($this->streetViewControl)) {
                    $this->output .='       ,streetViewControl: '.json_encode($this->streetViewControl).chr(10);
                    }
                    if(isset($this->tilt)) {
                    $this->output .='       ,tilt: '.$this->tilt.chr(10);
                    }
                    if(isset($this->zoomControl)) {
                    $this->output .='       ,zoomControl: '.json_encode($this->zoomControl).chr(10);
                    }
                    $this->output .='       }

                    var map = new google.maps.Map(document.getElementById(\''.$this->divName.'\'), mapOptions);
                    var directionsService = new google.maps.DirectionsService();
                    var geocoder          = new google.maps.Geocoder();
                    var bounds            = new google.maps.LatLngBounds();
                    var directionsDisplay = new google.maps.DirectionsRenderer();

                    directionsDisplay.setMap(map);

                    loadAddress(map,geocoder,bounds);
                    loadRoutes(map,directionsService,directionsDisplay);
                    loadPolygon(map);
                    loadMaker(map);
                    loadPolyLine(map);

                    }

                    function codeAddress(map,geocoder,bounds,address,title,icon,contentString) {

                        geocoder.geocode( { \'address\': address}, function(results, status) {

                        if (status == google.maps.GeocoderStatus.OK) {
                        bounds.extend(results[0].geometry.location); ';

                        if((strtolower($this->zoom)) == 'auto') {
                        $this->output .='map.fitBounds(bounds); ';
                        };

                        $this->output .='
                            var marker = new google.maps.Marker({
                            map: map,
                            title: title,
                            icon: icon,
                            position: results[0].geometry.location
                            });

                            if(contentString != null){
                            attachSecretMessage(map,marker, contentString);
                            }
                            } else if (status === google.maps.GeocoderStatus.OVER_QUERY_LIMIT) {
                            alert(\'The webpage has gone over the requests limit in too short a period of time! \');
                            } else if (status === google.maps.GeocoderStatus.ZERO_RESULTS) {
                                null;
                            } else {
                            alert(\'Geocode was not successful for the following reason: \' + status);
                            }
                        });
                        }';
                    $this->output .='

                    function attachSecretMessage(map,mapitem, contentString) {
                        var infowindow = new google.maps.InfoWindow(
                            { content: contentString
                            });
                        google.maps.event.addListener(mapitem, "click", function() {
                        console.log(\'>>>Click antes Open\');
                        infowindow.open(map,mapitem);
                        console.log(\'>>>Click antes Depois\');
                        });
                    }
                    function codeRoute(map,directionsService,directionsDisplay,start, end) {
                        var request = {
                            origin:start,
                            destination:end,
                            travelMode: google.maps.DirectionsTravelMode.'.$this->DirectionsTravelMode.'
                        };
                        directionsService.route(request, function(response, status) {
                        if (status == google.maps.DirectionsStatus.OK) {
                            directionsDisplay.setDirections(response);
                        }
                        });
                        }';

                    
                        
                    if($debug) { error_log('Funcao loadAddress'); };
                    //======================================================================================================================
                    //======================================================================================================================
                $this->output .='
                    function loadAddress(map,geocoder,bounds){
                        null;';

                    if(count($this->GmapsLocations) > 0){
                        foreach ($this->GmapsLocations as $key=>$value) {
                        $this->output .= chr(13).' codeAddress(map,geocoder,bounds,\''.$value['location_address'].'\',\''.$value['location_title'].'\',\''.$value['location_icon'].'\',\''.$value['location_content'].'\');';
                        }
                    }

                $this->output .='} ';

                    
                    if($debug) { error_log('Funcao loadRoutes'); };
                    //======================================================================================================================
                    //======================================================================================================================
                $this->output .='
                    function loadRoutes(map,directionsService,directionsDisplay){
                        null;';

                        if(count($this->GmapsRoutes) > 0){
                        foreach ($this->GmapsRoutes as $key=>$value) {
                        $this->output .= chr(13).' codeRoute(map,directionsService,directionsDisplay,\''.$value['location_address_start'].'\',\''.$value['location_address_end'].'\');';
                        }

                    }

                    $this->output .='} ';

                    if($debug) { error_log('Funcao loadPolygon'); };
                    //======================================================================================================================
                    //======================================================================================================================
                    $this->output .='
                    function loadPolygon(map){
                        null;';

                        if(count($this->GmapsPolygons) > 0) {
                            foreach ($this->GmapsPolygons as $key=>$value) {
                        $this->output .='
                                var polygonCoords = [];
                                vCoord = \''.$value['Polygon_Paths'].'\';
                                vCoord = vCoord.split(";");

                                for (var i = 0; i < vCoord.length; i++) {
                                    var lng = vCoord[i].split(\',\')[0];
                                    var lat = vCoord[i].split(\',\')[1];
                                polygonCoords.push({lat: Number(lat), lng: Number(lng) })
                                }

                                console.log(\'>>>Coordenadas Polygon id['.$value['Polygon_Id'].']:\'+JSON.stringify(polygonCoords));';

                                if( isset($value['Polygon_Title'])   &&   (isset($value['Polygon_TitleLatLng']))){
                                $this->output .='
                                        var MAPLABEL_'.$value['Polygon_Id'].' = new MapLabel({
                                            text: "'.$value['Polygon_Title'].'",
                                            position: new google.maps.LatLng('.explode(',',$value['Polygon_TitleLatLng'])[0].','.explode(',',$value['Polygon_TitleLatLng'])[1].'),
                                            map: map,
                                            fontSize: '.$value['Polygon_TitleFontSize'].',
                                            align: \'center\'
                                        }); ';
                                }

                            $this->output .='
                                var POLYGON_'.$value['Polygon_Id'].' = new google.maps.Polygon({
                                    paths          : polygonCoords,
                                    strokeColor    : \''.$value['Polygon_StrokeColor'].'\',
                                    strokeOpacity  : \''.$value['Polygon_StrokeOpacity'].'\',
                                    strokeWeight   : \''.$value['Polygon_StrokeWeight'].'\',
                                    fillColor      : \''.$value['Polygon_FillColor'].'\',
                                    fillOpacity    : \''.$value['Polygon_FillOpacity'].'\',
                                    geodesic       : '.$value['Polygon_Geodesic'].',
                                    draggable      : '.$value['Polygon_Draggable'].',
                                    editable       : '.$value['Polygon_Editable'].',
                                    zIndex         : -1,
                                    title          : "'.$value['Polygon_Title'].'"
                                    });
                                POLYGON_'.$value['Polygon_Id'].'.setMap(map);';

                                if( isset($value['Polygon_InfoWindow']) ) {
                            $this->output .='

                                    var contentString = \''.$value['Polygon_InfoWindow'].'\';
                                    var INFOWIN_'.$value['Polygon_Id'].' = new google.maps.InfoWindow({content: contentString});
                                    POLYGON_'.$value['Polygon_Id'].'.addListener("click", function(event) {
                                    INFOWIN_'.$value['Polygon_Id'].'.setPosition(event.latLng);
                                    INFOWIN_'.$value['Polygon_Id'].'.open(map, POLYGON_'.$value['Polygon_Id'].');
                                    });
                                    google.maps.event.addListener(map, \'click\', function() {
                                    INFOWIN_'.$value['Polygon_Id'].'.close();
                                    }); ';
                                
                                }

                            $this->output .='
                                var polygonCoords = [];';
                            }
                    }
                    

                $this->output .='}';
                    
                    if($debug) { error_log('Funcao loadMaker'); };
                    //======================================================================================================================
                    //======================================================================================================================
                $this->output .='
                    function loadMaker(map){
                        null;';

                        if(count($this->GmapsMakers) > 0) {
                            foreach ($this->GmapsMakers as $key=>$value) {
            
                            $this->output .='
                                var MAKER_LATLNG'.$value['Maker_Id'].' = new google.maps.LatLng('.$value['Maker_Lat'].','.$value['Maker_Lng'].');
                                console.log(\'>>>Coordenadas Maker id['.$value['Maker_Id'].']:\'+JSON.stringify(MAKER_LATLNG'.$value['Maker_Id'].'));';

                                if ($value['Maker_Problem'] == 'R') {
                                $this->output .=' var MAKER_ICON_'.$value['Maker_Id'].' = \'/'.$this->ContextUrl.'/app/images/makers/app-maker-red-dot.png\'';
                                }
                                elseif ($value['Maker_Problem'] == 'G') {
                                $this->output .=' var MAKER_ICON_'.$value['Maker_Id'].' = \'/'.$this->ContextUrl.'/app/images/makers/app-maker-green-dot.png\'';
                                }
                                elseif ($value['Maker_Problem'] == 'Y') {
                                $this->output .=' var MAKER_ICON_'.$value['Maker_Id'].' = \'/'.$this->ContextUrl.'/app/images/makers/app-maker-yellow-dot.png\'';
                                }
                                else {
                                $this->output .=' var MAKER_ICON_'.$value['Maker_Id'].' = \'/'.$this->ContextUrl.'/app/images/makers/app-maker-green-dot.png\'';
                                }

                            $this->output .='
                                var MAKER_'.$value['Maker_Id'].' = new google.maps.Marker({
                                position: MAKER_LATLNG'.$value['Maker_Id'].',
                                map: map,
                                icon: MAKER_ICON_'.$value['Maker_Id'].',
                                title: \''.$value['Maker_Title'].'\' });';

                                if(isset($value['Maker_InfoWindow'])){

                                $this->output .='
                                    var contentString = \''.$value['Maker_InfoWindow'].'\';
                                    var INFOWIN_MAKER_'.$value['Maker_Id'].' = new google.maps.InfoWindow({content: contentString});
                                    MAKER_'.$value['Maker_Id'].'.addListener("click", function(event) {
                                    INFOWIN_MAKER_'.$value['Maker_Id'].'.setPosition(event.latLng);
                                    INFOWIN_MAKER_'.$value['Maker_Id'].'.open(map, MAKER_'.$value['Maker_Id'].'); });
                                    google.maps.event.addListener(map, \'click\', function() { INFOWIN_MAKER_'.$value['Maker_Id'].'.close(); }); ';

                                    }

                        };
                    };
                    $this->output .='}';


                    if($debug) { error_log('Funcao loadPolyLine'); };
                    //======================================================================================================================
                    //======================================================================================================================                 
                $this->output .='

                    function loadPolyLine(map){
                        null;';

                        if(count($this->GmapsPolylines) > 0) {
                            foreach ($this->GmapsPolylines as $key=>$value) {
                            $this->output .='
                                    var polylineCoords = [];

                                    vCoord = \''.$value['Polyline_Paths'].'\';
                                    vCoord = vCoord.split(";");

                                    for (var i = 0; i < vCoord.length; i++) {
                                        var lng = vCoord[i].split(\',\')[0];
                                        var lat = vCoord[i].split(\',\')[1];
                                    polylineCoords.push({lat: Number(lat), lng: Number(lng) })
                                    }

                                    console.log(\'>>>Coordenadas PolyLine id['.$value['Polyline_Id'].']:\'+JSON.stringify(polylineCoords));';

                                $this->output .='
                                    var POLYLINE_'.$value['Polyline_Id'].' = new google.maps.Polyline({
                                    path           : polylineCoords,
                                    strokeColor    : \''.$value['Polyline_StrokeColor'].'\',
                                    strokeOpacity  : \''.$value['Polyline_StrokeOpacity'].'\',
                                    strokeWeight   : \''.$value['Polyline_StrokeWeight'].'\',
                                    geodesic       : '.$value['Polyline_Geodesic'].'
                                    });
                                    POLYLINE_'.$value['Polyline_Id'].'.setMap(map);';

                                $this->output .='';

                                }
                            }
                        $this->output .='}';

                    //TODO TokenMaps na TCONFIG
                $this->output .='
                    </script>
                    <script async defer
                        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCYNNFwLMa4pra-C7A3x8a_cQHCuJdlOnw&callback=initMap&libraries=places&libraries=drawing" type="text/javascript">
                    </script>
                    </head>
                    </html>';

                    (string)$arquivo = 'app/output/'. $pMapFileName .'.html';
                    file_put_contents($arquivo,  $this->output);

                    return '/'.$arquivo;
            }
            catch (Exception $e)
            {
                error_log('Erro Gmaps.php - '.$e->getMessage());
            }

    }

}