let bannerIndex=0;
let bannerList=[];
    
function getBanner(contextPath){
	let banner = $("#banner");
    	
    	//서버와 통신
    	$.ajax({
    		url:contextPath+"/banners",
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
}// getBannerEnd

/////////////////////////////////////////
/*
  로그아웃
*/
function logout(contextPath){
	alert("로웃함수....")
	location.href=contextPath+"/logout";//get방식
}















