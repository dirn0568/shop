var maxCount = 3;								// 카운트 최대값은 2
var count = 0;   								// 카운트, 0으로 초기화 설정
console.log("02-07실행중")
var maxCount2 = 3;
var count2 = 0;

function CountChecked(field){
    console.log("체크함수실행중")
    if (field.checked) {
        count += 1;								// count 1 증가
    }
    else {										// 아니라면 (field의 속성이 checked가 아니라면)
        count -= 1;								// count 1 감소
    }

    if (count > maxCount) {						// 만약 count 값이 maxCount 값보다 큰 경우라면
        alert("최대 3개까지만 선택가능합니다!");	// alert 창을 띄움
        field.checked = false;						// (마지막 onclick한)field 객체의 checked를 false(checked가 아닌 상태)로 만든다.
        count -= 1;									// 이때 올라갔던 카운트를 취소처리해야 하므로 count를 1 감소시킨다.
    }
}

function CountChecked2(field){
    console.log("체크함수실행중")
    if (field.checked) {
        count2 += 1;
    }
    else {
        count2 -= 1;
    }

    if (count2 > maxCount2) {
        alert("최대 3개까지만 선택가능합니다!");
        field.checked = false;
        count2 -= 1;
    }
}