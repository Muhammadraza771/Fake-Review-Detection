$(function(){
     
        chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function 
        (tabs) {
            urlPresent = tabs[0].url;
       
          

           chrome.storage.sync.set({'url': urlPresent})
        });

            

         $("#startbutton").click(function(){
     
      
            chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function 
            (tabs) {
                urlPresent = tabs[0].url;
               // alert(urlPresent)
                //var myWindow = window.open("http://localhost:3000/", "_blank");
                //myWindow.document.write("<h1> urlPresent</h1> "+urlPresent);
               // window.open('http://localhost:3000/', '_blank');

           
               
              
            });

           

        window.open('http://localhost:3000/?'+urlPresent, '_blank');
        

      

        
    })


     


})


