
let holidays = ['03-01', '07-17', '08-15', '10-03', '10-09'];

function isHoliday(dateString) {
  let result = false;

  holidays.forEach(e=>{
    if(e === `${dateString.split('-')[1]}-${dateString.split('-')[2]}`) result = true;
  });

  return result;
}


// 날짜 두개 잡는 거 짜봅시당.
let selDate1 = undefined;
let selDate2 = undefined;


//페이지 로드 시 현재 날짜로 달력 제목 세팅해주는 이벤트입니다.
document.addEventListener('DOMContentLoaded', () => {
  let a = new Date();
  let year = a.getFullYear();
  let month = getMonthInEng(a.getMonth() + 1);
  document.getElementById('dateTitle').innerText = `${year}년 ${month}`;
  document.getElementById('dateTitle').dataset.date = a;

  dateSelectEffect();

  preNextEvent();

  document.getElementById('submit').addEventListener('click', () => {
    if (document.getElementById('yearspan').innerText === "") {
      alert('날짜를 선택해주세요');
      return;
    }

    let year = document.getElementById('yearspan').innerText;
    let month = document.getElementById('monthspan').innerText;
    let date = document.getElementById('datespan').innerText;
    let day = document.getElementById('dayspan').innerText;
    let year2 = document.getElementById('yearspan2').innerText;
    let month2 = document.getElementById('monthspan2').innerText;
    let date2 = document.getElementById('datespan2').innerText;
    let day2 = document.getElementById('dayspan2').innerText;

    // 테이블 초기화
    document.querySelectorAll('div.table').forEach((e,i)=>{
      if(i > 0) e.remove();
    });

    // 테이블 작성
    let start = new Date(year, month-1, date);
    let end = new Date(year2, month2-1, date2);

    for(let i = start.getTime(); i <= end.getTime(); i+= 86400*1000) {
      let d = new Date(i);

      let month = d.getMonth()+1;
      if(month < 10) month = "0" + month;
      let date = d.getDate();
      if(date < 10) date = "0" + date;

      document.getElementById('tableWrapper').innerHTML +=
        `<div class="table">`+
        `<div class="tableDate">${d.getFullYear()}-${month}-${date}</div>`+
        `<div class="day">${getDayInKorFromIndex(d.getDay())}</div>`+
        `<div class="isHoliday">아니오</div>`+
        `</div>`;
    }


    //토요일 일요일 국경일 컬러처리
    document.querySelectorAll('div.day').forEach(e=>{
      if(e.innerText === "토") e.parentElement.style.color="blue";
      if(e.innerText === "일") e.parentElement.style.color="red";
    });

    //국경일 처리
    document.querySelectorAll('div.tableDate').forEach(e=>{
      if(isHoliday(e.innerText)) {
        e.parentElement.lastChild.innerText = "예";
        e.parentElement.style.color="red";
        e.parentElement.style.fontWeight="550";
      }
    });
    selDate1 = undefined;
    selDate2 = undefined;
  });
});

//조회 버튼에 클릭 이벤트 적용.
//두 개의 날짜를 선택 한 다음 조회를 눌렀을 때 달력에 날짜가 조회되어야 함.
document.getElementById('searchButton').addEventListener('click', () => {

  let firstDate = document.getElementById('firstDate');
  let secondDate = document.getElementById('secondDate');

  //1. null 검증
  if (firstDate.value === "") {
    alert('탐색 시작 날짜를 선택해주세요');
    firstDate.focus();
    return;
  }
  if (secondDate.value === "") {
    alert('탐색 마지막 날짜를 선택해주세요');
    secondDate.focus();
    return;
  }

  //2. firstDate < secondDate 검증
  if (firstDate.value > secondDate.value) {
    alert('탐색 마지막 날짜를 시작 날짜 이후로 선택해주세요');
    secondDate.value = "";
    secondDate.focus();
    return;
  }

  //2-1. 기존 달력 내용을 제거합니다.
  clearCalendar();

  //3. 날짜 표시 및 날짜별 클릭 이벤트 적용
  let dateTitle = document.getElementById('dateTitle');
  let date1 = firstDate.value;
  let date2 = secondDate.value;

  let newTitle = `${date1.split('-')[0]}년 `;
  newTitle += getMonthInEng(parseInt(date1.split('-')[1]));
  dateTitle.innerText = newTitle; // 여기까지 달력 제목 출력 완료.
  dateTitle.dataset.date = date1;

  // 시작 날짜의 연, 월, 일, 요일
  let fy = new Date(Date.parse(document.getElementById('firstDate').value)).getFullYear();
  let fm = new Date(Date.parse(document.getElementById('firstDate').value)).getMonth();
  let fd = new Date(Date.parse(document.getElementById('firstDate').value)).getDate();
  let fday = new Date(Date.parse(document.getElementById('firstDate').value)).getDay();

  // 종료 날짜의 연, 월, 일, 요일
  let sy = new Date(Date.parse(document.getElementById('secondDate').value)).getFullYear();
  let sm = new Date(Date.parse(document.getElementById('secondDate').value)).getMonth();
  let sd = new Date(Date.parse(document.getElementById('secondDate').value)).getDate();
  let sday = new Date(Date.parse(document.getElementById('secondDate').value)).getDay();

  let start = new Date(fy, fm, fd);
  let end = new Date(sy, sm, sd);

  // 시작 날짜의 첫번째 요일 설정
  let firstDayOfThisMonth = new Date(fy, fm, 1).getDay();
  let lastDate = getLastDateOfMonth(fy, fm + 1);

  let tds = new Array();
  let td = document.querySelectorAll('td');

  for (let i = 0; i < lastDate; i++) {
    tds.push(td[7 + firstDayOfThisMonth + i]);
  }

  // 해당 월의 전체 날짜를 출력합니다.
  tds.forEach((e, i) => {
    e.innerText = i + 1;
    e.dataset.date = new Date(fy, fm, i + 1);
  });

  // 범위에서 벗어난 날짜를 제거합니다.
  document.querySelectorAll('td').forEach(e => {
    if (new Date(e.dataset.date) < new Date(fy, fm, fd)) e.innerText = "";
    if (new Date(e.dataset.date) > new Date(sy, sm, sd)) e.innerText = "";
  });

  // 날짜 클릭 시 하단 텍스트에 표시되도록 이벤트 연결합니다.
  tds.forEach(e => e.addEventListener('click', () => {
    if (e.innerText !== "") {
      // 첫 날짜 선택일 경우
      if(selDate1 === undefined) {
        let date = document.getElementById('dateTitle').dataset.date.split('-');
        document.getElementById('yearspan').innerText = date[0];
        document.getElementById('monthspan').innerText = date[1];
        document.getElementById('datespan').innerText = document.getElementById('dateTitle').dataset.datedate;
        document.getElementById('dayspan').innerText = getDayInKorFromEng(e.className);
        selDate1 = new Date(date[0], parseInt(date[1])-1, document.getElementById('dateTitle').dataset.datedate);

        // 두번째 날짜 선택일 경우
      }else {
        //첫번째 날짜가 더 이전 날짜인 경우 (정상 순서);
        selDate2 = e.dataset.date;
        if(new Date(selDate2) > new Date(selDate1)) {
          document.getElementById('yearspan2').innerText = new Date(selDate2).getFullYear();
          document.getElementById('monthspan2').innerText = new Date(selDate2).getMonth()+1;
          document.getElementById('datespan2').innerText = new Date(selDate2).getDate();
          document.getElementById('dayspan2').innerText = getDayInKorFromEng(e.className);
        }
        //두번쨰 날짜가 더 이전 날짜인 경우 (역순);
        else {
          // selDate1 과 selDate2 값 교환
          let temp = selDate1;
          selDate2 = new Date(selDate1);
          selDate1 = new Date(temp);

          // 1에 selDate1 집어넣기
          document.getElementById('yearspan').innerText = new Date(selDate1).getFullYear();
          document.getElementById('monthspan').innerText = new Date(selDate1).getMonth()+1;
          document.getElementById('datespan').innerText = new Date(selDate1).getDate();
          document.getElementById('dayspan').innerText = getDayInKorFromEng(e.className);

          // 2에 selDate2 집어넣기
          document.getElementById('yearspan2').innerText = new Date(selDate2).getFullYear();
          document.getElementById('monthspan2').innerText = new Date(selDate2).getMonth()+1;
          document.getElementById('datespan2').innerText = new Date(selDate2).getDate();
          document.getElementById('dayspan2').innerText = getDayInKorFromEng(e.className);
        }

      }

    }
  }));
  selDate1 = undefined;
  selDate2 = undefined;

  document.getElementById('yearspan').innerText = "";
  document.getElementById('monthspan').innerText = "";
  document.getElementById('datespan').innerText = "";
  document.getElementById('dayspan').innerText = "";
  document.getElementById('yearspan2').innerText = "";
  document.getElementById('monthspan2').innerText = "";
  document.getElementById('datespan2').innerText = "";
  document.getElementById('dayspan2').innerText = "";
});



//4. 이전, 다음 버튼 클릭 이벤트 적용
function preNextEvent() {


  // 다음 버튼 먼저
  document.getElementById('next').addEventListener('click', ()=>{
    // null 검증
    if(document.getElementById('firstDate').value==="" || document.getElementById('secondDate').value===""){
      alert('날짜를 먼저 선택해주세요');
      return;
    }

    let maxMonth = new Date(document.getElementById('secondDate').value);
    let thisMonth = new Date(document.getElementById('dateTitle').dataset.date);

    if(maxMonth > thisMonth && maxMonth.getMonth() !== thisMonth.getMonth()) {
      // 다음달 표시 구현해야함

      // 1. 달력 다 지우기
      clearCalendar();

      // 2. 달력 제목, 제목 date dataset 변경
      let year = document.getElementById('dateTitle').innerText.split('년 ')[0];
      let month = document.getElementById('dateTitle').innerText.split('년 ')[1];
      let next = getNextYearMonth(year, month);
      document.getElementById('dateTitle').innerText = `${next.year}년 ${next.month}`;
      document.getElementById('dateTitle').dataset.date = `${next.year}-${next.monthNumber}-01`;

      // 3. 달력 다 그리기
      // 해당 월의 전체 날짜를 출력합니다.
      let targetMonth = new Date(document.getElementById('dateTitle').dataset.date);
      let lastDate = getLastDateOfMonth(targetMonth.getFullYear(), targetMonth.getMonth()+1);
      let day = targetMonth.getDay();
      let arr = new Array();
      document.querySelectorAll('td').forEach((e,i)=>{
        if(i > 6 + day && i <= 6+day+lastDate) {
          e.innerText = i-6-day;
          e.dataset.date = new Date(next.year, next.monthNumber-1, e.innerText);
        }
      });

      // 4. 범위 바깥 날짜 지우기
      document.querySelectorAll('td').forEach(e=>{
        let maxdate = new Date(document.getElementById('secondDate').value);
        if(new Date(e.dataset.date) > maxdate) {
          e.innerText="";
          e.dataset.date = undefined;
        }
      });

    }else {
    }
    clearSelectedDate();
  });

  // 이전 버튼 ㄱㄱ
  document.getElementById('pre').addEventListener('click', ()=>{
    // null 검증
    if(document.getElementById('firstDate').value==="" || document.getElementById('secondDate').value===""){
      alert('날짜를 먼저 선택해주세요');
      return;
    }
    let minMonth = new Date(document.getElementById('firstDate').value);
    let thisMonth = new Date(document.getElementById('dateTitle').dataset.date);

    if(minMonth < thisMonth) {
      //이전달 표시 구현해야함

      // 1. 달력 다 지우기
      clearCalendar();

      // 2. 달력 제목, 제목 date dataset 변경
      let year = document.getElementById('dateTitle').innerText.split('년 ')[0];
      let month = document.getElementById('dateTitle').innerText.split('년 ')[1];
      let pre = getPreYearMonth(year, month);
      document.getElementById('dateTitle').innerText = `${pre.year}년 ${pre.month}`;
      document.getElementById('dateTitle').dataset.date = `${pre.year}-${pre.monthNumber}-01`;

      // 3. 달력 다 그리기
      let targetMonth = new Date(document.getElementById('dateTitle').dataset.date);
      let lastDate = getLastDateOfMonth(targetMonth.getFullYear(), targetMonth.getMonth()+1);
      let day = targetMonth.getDay();
      let arr = new Array();
      document.querySelectorAll('td').forEach((e,i)=>{
        if(i > 6 + day && i <= 6+day+lastDate) {
          e.innerText = i-6-day;
          e.dataset.date = new Date(pre.year, pre.monthNumber-1, e.innerText);
        }
      });

      // 4. 범위 바깥 날짜 지우기
      document.querySelectorAll('td').forEach(e=>{
        let mindate = new Date(document.getElementById('firstDate').value);
        mindate.setHours(0,0,0,0);
        if(new Date(e.dataset.date) < mindate) {
          e.innerText="";
          e.dataset.date = undefined;
        }
        if(new Date(e.dataset.date).getDate() === mindate.getDate()) {
          e.innerText = mindate.getDate();
          e.dataset.date = new Date(pre.year, pre.monthNumber-1, e.innerText);
        }
      });

    }else {
    }

    clearSelectedDate();

  });

}

// 이전, 다음 눌렀을 때 선택 값을 없애는 함수입니다.
function clearSelectedDate() {
  document.querySelectorAll('td').forEach((e,i)=>{
    if(i>6) e.style.backgroundColor = "transparent";
  });
}


// 달력 초기화 함수입니다.
function clearCalendar() {
  document.querySelectorAll('td').forEach((e, i) => {
    if (i > 6) e.innerText = "";
  });
}


// 날짜를 클릭했을 때 배경색을 넣어주는 이벤트 함수입니다.
function dateSelectEffect() {
  document.querySelectorAll('td').forEach((e,i) => e.addEventListener('click', () => {
    if(i < 7) return;
    if (e.innerText !== "") {
      document.querySelectorAll('td').forEach((e, i) => {
        if (i > 6) e.style.backgroundColor = "transparent";
      });
      e.style.backgroundColor = "rgb(128, 193, 219)";
      document.getElementById('dateTitle').dataset.datedate = e.innerText;
    }
  }));
}

// 영어 3자로 된 요일을 받아서 한글 한 글자 요일로 반환하는 함수입니다.
function getDayInKorFromEng(day) {
  let result = '';
  switch (day) {
    case 'mon': result = "월"; break;
    case 'tue': result = "화"; break;
    case 'wed': result = "수"; break;
    case 'thu': result = "목"; break;
    case 'fri': result = "금"; break;
    case 'sat': result = "토"; break;
    case 'sun': result = "일"; break;
  }
  return result;
}

// 숫자로 월을 받아서 마지막 날짜를 리턴해주는 함수입니다.
function getLastDateOfMonth(year, month) {
  let lastDateArray = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let lastDate = lastDateArray[month - 1];
  //윤년 처리
  if (year % 4 === 0 && month === 2) lastDate = 29;
  return lastDate;
}

// 숫자로 월을 받아서 3자리 약자로 리턴해주는 함수입니다.
function getMonthInEng(month_as_number) {
  let mon = '';
  switch (month_as_number) {
    case 01: mon = 'Jan'; break;
    case 02: mon = 'Feb'; break;
    case 03: mon = 'Mar'; break;
    case 04: mon = 'Apr'; break;
    case 05: mon = 'May'; break;
    case 06: mon = 'Jun'; break;
    case 07: mon = 'Jul'; break;
    case 08: mon = 'Aug'; break;
    case 09: mon = 'Sep'; break;
    case 10: mon = 'Oct'; break;
    case 11: mon = 'Nov'; break;
    case 12: mon = 'Dec'; break;
  }
  return mon;
}

function getDayInKorFromIndex(i) {
  let days = ['일', '월', '화', '수', '목', '금', '토'];
  return days[i];
}


// 연도와 월을 전달해서 다음 월과 연도를 반환하는 함수입니다
function getNextYearMonth(year, month) {
  let result = new Object();
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  months.forEach((e,i)=>{
    if(e === month) {
      if(i === 11) {
        result.month = months[0];
        result.monthNumber = 1;
        result.year = parseInt(year)+1;
      }
      else {
        result.month = months[i+1];
        result.monthNumber = i+2;
        result.year = year;
      }
    }
  });
  if(result.monthNumber < 10) {
    result.monthNumber = "0"+result.monthNumber;
  }
  return result;
}

// 연도와 월을 전달해서 이전 월과 연도를 반환하는 함수입니다
function getPreYearMonth(year, month) {
  let result = new Object();
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  months.forEach((e,i)=>{
    if(e === month) {
      if(i === 0) {
        result.month = months[11];
        result.monthNumber = 12;
        result.year = year-1;
      }
      else {
        result.month = months[i-1];
        result.monthNumber = i;
        result.year = parseInt(year);
      }
    }
  });

  if(result.monthNumber < 10) {
    result.monthNumber = "0"+result.monthNumber;
  }
  return result;
}