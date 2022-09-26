function initMap() {

  var options = {
         zoom :12,
         center :{ lat: -37.844091, lng: 145.003759 }}
  // The map, centered at Uluru
  var map = new google.maps.Map(document.getElementById("map"), options);
  /* listen for clicks
  google.maps.event.addListener(map,'click',function(event){
      addMarker({ coord:event.latLng

      });
      });
   */


  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: { lat: -37.844091, lng: 145.003759 },
    map: map,
  });


  var infoWindow = new google.maps.InfoWindow({
       content : 'camping'});
  marker.addListener('click', function(){
       infoWindow.open(map,marker);
       })

  function addMarker(props){
    const marker = new google.maps.Marker({
        position: props.coord,
        map: map,
         });
    //icon :props.iconImg
    //check icon
    if (props.iconImg){
        marker.setIcon(props.iconImg);}

    if (props.content){
        var infoWindow = new google.maps.InfoWindow({
            content: props.content
           });
        marker.addListener('click', function(){
        infoWindow.open(map,marker);
        });
       }
    }

  // list of markers here
  var markers = [{coord:{lat:-37.840658,lng:145.000981},
              iconImg:'https://img.icons8.com/ios-filled/20/000000/basketball.png',
              content :'<a>traininng</a>'
              },
              {coord:{lat:-37.844860,lng:144.990770}
              }
  ]

  // loop all markers

  for (var i =0 ; i < markers.length; i++){

    addMarker(markers[i]);
  }
/*
  addMarker ({coord:{lat:-37.840658,lng:145.000981},
              iconImg:'https://img.icons8.com/ios-filled/20/000000/basketball.png',
              content :'<a>traininng</a>'
              })

  addMarker ({coord:{lat:-37.844860,lng:144.990770}});
*/
}

window.initMap = initMap;