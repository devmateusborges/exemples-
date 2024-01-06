var map;
var idInfoBoxAberto;
var infoBox = [];
var markers = [];
var polylines = [];

function initialize() {	
	var latlng = new google.maps.LatLng(-20.58252,-47.86284);
	
    var options = {
        zoom: 5,
		center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById("mapa"), options);
}

initialize();

function abrirInfoBox(id, marker) {
	if (typeof(idInfoBoxAberto) == 'number' && typeof(infoBox[idInfoBoxAberto]) == 'object') {
		infoBox[idInfoBoxAberto].close();
	}

	infoBox[id].open(map, marker);
	idInfoBoxAberto = id;
}

function carregarPontos() {

	$.get( "http://sistemapcb.net.br/api/testes/getPontos", function( pontos ) {
		
	//  });	
	
//$.getJSON('js/pontos1.json', function(pontos) {
		
		var latlngbounds = new google.maps.LatLngBounds();
		
		polylines=pontos;
		$.each(pontos, function(index, ponto) {
			
			var marker = new google.maps.Marker({
				position: new google.maps.LatLng(ponto.Latitude, ponto.Longitude),
				title: "Meu ponto personalizado! :-D",
				icon: 'img/marcador.png'
			});
			
			var myOptions = {
				content: "<p>" + ponto.Descricao + "</p>",
				pixelOffset: new google.maps.Size(-150, 0)
        	};

			infoBox[ponto.Id] = new InfoBox(myOptions);
			infoBox[ponto.Id].marker = marker;
			
			infoBox[ponto.Id].listener = google.maps.event.addListener(marker, 'click', function (e) {
				abrirInfoBox(ponto.Id, marker);
			});
			
			markers.push(marker);
			
			latlngbounds.extend(marker.position);
			
		});
		

		
        var flightPlanCoordinates = [
			{lat: -20.772, lng: -47.214},
			{lat: -21.291, lng: -48.821},
			{lat: -22.142, lng: -49.431},
			{lat: -23.467, lng: -50.027}
		  ];
		  var flightPath = new google.maps.Polyline({
			path: flightPlanCoordinates,
			geodesic: true,
			strokeColor: '#FF0000',
			strokeOpacity: 1.0,
			strokeWeight: 2
		  });
  
		  flightPath.setMap(map);3
  
		  
		  var markerCluster = new MarkerClusterer(map, markers,flightPath);

		map.fitBounds(latlngbounds);
		
	});
	
}

carregarPontos();