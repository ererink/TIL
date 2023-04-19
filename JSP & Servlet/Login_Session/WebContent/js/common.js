$(function() {
  // Logout function
  function logout() {
    $.ajax({
      url: "LoginServlet",
      type: "post",
      data: {
        action: "logout"
      },
      success: function() {
        window.location.replace("index.jsp");
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log("Error: " + textStatus);
      }
    });
  }
});


let bannerIndex=0;
let bannerList=[];


$(function(){
	let banner = $("#banner");
	
	//서버와 통신
	$.ajax({
		url:"banners",
		type:"get",
		dataType:"json",
		success: function(result, status, xhr){
			console.log("result = "+result)
			console.log("status = "+status)
			console.log("xhr = "+xhr)
			
			bannerList = result.banners;
			console.log("bannerList = "+bannerList)
			
			let bannerText = bannerList[bannerIndex++];
			banner.text(bannerText);
			
			setInterval(function(){
				let bannerText = bannerList[bannerIndex++];
    			banner.text(bannerText);
    			
    			if(bannerIndex==bannerList.length) bannerIndex=0;
    			
    			
			}, 3000);
			
		},
		error : function(jqXHR, textStatus, errorThrown){
			alert("문제 발생 : " + jqXHR.status)
		}
	
		
	});
	
	
	 //버튼 클릭했을대
	 $(".main-item-btn").click(function(){
		 let idValue =  $(this).closest(".main-item").attr("data-main-item-id");
		 console.log(idValue)
	 });
});
    