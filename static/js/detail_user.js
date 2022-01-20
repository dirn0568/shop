
document.getElementById('bizFile').addEventListener('change', function(){
    console.log('실행중?111')
    var filename = document.getElementById('fileName');
    if(this.files[0] == undefined){
        filename.innerText = '';
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

document.getElementById('bizFile1').addEventListener('change', function(){
    console.log('실행중?222')
    var filename1 = document.getElementById('fileName1');
    if(this.files[0] == undefined){
        filename1.innerText = '';
        return;
    }
    if (this.files[0].name.length > 5) {
        for (i = 0; i < 5; i++) {
            filename1.innerText += this.files[0].name[i];
        }
        filename1.innerText += '...';
    }
    else {
        filename1.innerText += this.files[0].name;
    }
});