var count = 0;
console.log("02-07실행중")

function propose_okay(propose, title, pk){
    if (!confirm("휴대폰 번호와 이메일을 정말로 보내시겠습니까.")) {
        temp = 'http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail=1';
        console.log(temp);
        alert("취소 되었습니다.");
    } else {
        alert("휴대폰 번호와 이메일을 성공적으로 보냈습니다.");
        temp = 'http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail=1';
        console.log(temp);
        window.open('http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail=1', "네이버" ,"top=100px, left=100px, height=800px, width=1200px");
        window.location.href='http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail=1';
    }
}

function propose_okay2(propose, title, pk){
    if (!confirm("정말로 면접제의를 거절하시겠습니까.(거절 메세지가 제안자에게 전달됩니다)")) {
        alert("취소 되었습니다.");
    } else {
        alert("거절하셨습니다");
        temp = 'http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail=2';
        console.log(temp);
        window.open('http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail2=1', "네이버" ,"top=100px, left=100px, height=800px, width=1200px");
        window.location.href='http://3.39.239.247/message/message_propose_detail/' + title + '/' + pk + '?detail2=1';
    }
}