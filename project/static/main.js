

var rand = function() {
    return Math.random().toString(36).substr(2); // remove `0.`
};

var token = function() {
    return rand() + rand(); // to make it longer
};

function login()
{
    var un = document.loginform.usr.value;
    var pwd = document.loginform.pword.value;
    var username = "rejani2906@gmail.com";
    var password = "1234567"
    var reg = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(un =='')
    {
        alert("Please enter user name.");
    }
    else if(pwd=='')
    {
        alert("Enter the password");
    }
    else if(!reg.test(un))
    {
        alert("Enter valid email id.");
    }
    else if(pwd.length < 6)
    {
        alert("Password minimum length is 6.");
    }
    else
    {
        if((un==username)&&(pwd==password)){
            localStorage.setItem('key',token());
            console.log(localStorage);           
            window.location.href="upload.html";
            /*return true;*/
        }
        else{
            alert('Login was unsuccessful, please check your username and password');
            return false;
        }
    
    }
}		
 
function logout(){
    localStorage.removeItem('key');
    console.log(localStorage); 
    window.location.href="home.html"; 
}


