var $snup = null;
$(document).ready(function(){
    //함수 호출
    initialize();
    moveE();
});
//전역변수를 초기화
function initialize(){
    //스누피 찾기
    $snup = $("#snupy");
}
//이벤트와 관련된 내용을 함수로 등록
function moveE(){
    //버튼에 이벤트 등록
    $("#btnS").click(function(){
        //스누피 움직이기
        //스누피 위치 값 구하기
        var x = parseInt($("#textX").val());    //val()은 가져오는 값을 실제 값으로 만들어줌
        var y = parseInt($("#textY").val());
        moveSnup(x, y);
    })
} 
//스누피의 움직이는 기능을 구현해놓은 함수
function moveSnup(x, y){
    if((0 <= x <= 500) && (0 <= y <= 300)){
            $snup.animate({left:x, top:y}, 1000);
        }else{
            alert("입력된 값이 범위를 벗어났습니다.");
        }
}