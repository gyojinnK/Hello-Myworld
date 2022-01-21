$(document).ready(function(){
    //지구이미지 웹요소(노드)를 찾아서 저장
    var $earth = $("#earth");
    //버튼에 이벤트를 등록
    $("#btnStart").click(function(){
        $earth.animate({
            rotate : "360deg"
        }, 1000);
    })
});
