
document.getElementById('bizFile').addEventListener('change', function(){
    console.log('실행중?111')
    var filename = document.getElementById('fileName');
    if(this.files[0] == undefined){
        filename.innerText = '이미지등록';
        return;
    }
    if (this.files[0].name.length > 5) {
        for (i = 0; i < 5; i++) {
            filename.innerText += this.files[0].name[i];
        }
        filename.innerText += '...';
    }
    else {
        filename.innerText += this.files[0].name;
    }
});