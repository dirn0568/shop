var count = 0;
console.log("02-07실행중")

function search_propose(propose, pk){
    if (!confirm("확인(예) 또는 취소(아니오)를 선택해주세요.")) {
        alert("취소 되었습니다.");
    } else {
        window.location.href="http://3.39.239.247/search/search_resume?title=" + pk;
        alert("면접제의 메일을 성공적으로 보냈습니다.");
    }
}