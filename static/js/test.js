var test1 = document.getElementById('male');
var test2 = document.getElementById('female');
function choice(){
    console.log('이거 왜 안됌')
    test1 = document.getElementById('male');
    test2 = document.getElementById('female');
    if(document.getElementById('male').checked) {
      alert("남자 선택");
    }else if(document.getElementById('female').checked) {
      alert("여자 선택");
    }else {
      alert("선택없음");
    }
}

while(true) {
    choice();
}

//window.onload = function(){
//            console.log('남자 ' + document.getElementById('male').checked);
//            console.log('여자 ' + document.getElementById('female').checked);
//        };
//        11-24 버튼 클릭여부 자바스크립트로 확인할려고 하는데 하 그냥 잘모르겠음