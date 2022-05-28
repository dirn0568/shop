var count = 0;
console.log("02-07실행중")

function resume_propose(propose, pk){
    if (!confirm("확인(예) 또는 취소(아니오)를 선택해주세요.")) {
        alert("취소 되었습니다.");
    } else {
        alert("면접제의 메일을 성공적으로 보냈습니다.");
        window.location.href='3.39.239.247/resume/detail_resume/' + pk + '?resume_propose=' + pk;
    }
}