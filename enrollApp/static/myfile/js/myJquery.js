

form=document.getElementById('myForm');

form.addEventListener('submit', FormSubmitFunction);

function FormSubmitFunction(e){
       e.preventDefault();

       // url user korte hoile method user korte hobe   example method: "POST", url: "{% url 'formDatabase' %}",
      // location  user korte hoile type user korte hoibe example type: "POST",  url:"form-send_database/"
       $.ajax({
        method: "POST",
        url:"form-send_database/",
        data:$("#myForm").serialize(),
        dataType:'json',

        success: successfunction

      });
  }


  function successfunction(data){
      let x = data.st_data; // views.py inset
      let len=x.length
      let output=""
    if(data.msg === "save"){
        for(let i=0;i<len;i++){
            output+="<tr><td>" + x[i].id + "</td><td>" + x[i].name + "</td><td>" +
                 x[i].email + "</td><td>" +  x[i].password +
                "</td><td> <input type='button' class='btn btn-warning btn-sm' value='Edit'  +  data-sid="+ x[i].id +" \>" +
                " <input type='button' class='btn btn-danger btn-sm' value='Delete'  +  data-sid="+ x[i].id +" \> " + "</tr></td>"

        }
        $("#Tbody").html(output)
        document.getElementById('myForm').reset()
        alert("form is Submit !");
    }
    if(data.msg===0){
        alert("form is not Submit !");
        console.log("form is not Submit ");
    }

}
