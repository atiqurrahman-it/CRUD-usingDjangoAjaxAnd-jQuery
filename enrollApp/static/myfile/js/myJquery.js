

form=document.getElementById('myForm');
// create and read data
form.addEventListener('submit', FormSubmitFunction);

function FormSubmitFunction(e){
       e.preventDefault();
       //sid=document.getElementById('studId');
        studentInformation=$("#myForm").serialize()
        console.log(studentInformation)
       // url user korte hoile method user korte hobe   example method: "POST", url: "{% url 'formDatabase' %}",
      // location  user korte hoile type user korte hoibe example type: "POST",  url:"form-send_database/"
       $.ajax({
        method: "POST",
        url:"form-send_database/",
        data:studentInformation,
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
                "</td><td> <input type='button' class='btn btn-warning btn-sm btn-edit' value='Edit'  +  data-sid="+ x[i].id +" >" +
                " <input type='button' class='btn btn-danger btn-sm btn-delete' value='Delete'  +  data-sid="+ x[i].id +" > " + "</tr></td>"
             }
            $("#Tbody").html(output)
            $("#studId").val("");
            document.getElementById('myForm').reset()
            //alert("form is Submit !");
       }
    if(data.msg===0){
        $('#studId').val("")
        alert("form is not Submit !");
        console.log("form is not Submit ");
    }

 }

// Delete data

$("#Tbody").on('click','.btn-delete',function(){
    let id=$(this).attr("data-sid")
    let csf= $('input[name=csrfmiddlewaretoken]').val()
    let mydata={sid:id,csrfmiddlewaretoken:csf};
    mythis=this;
     $.ajax({
         //url:"{% url 'delete' %}",
         method: "POST",
         url:"deletedata/",
         data:mydata,
        success:  deleteSuccessFunction


      });
});

//data value  import views.py
function deleteSuccessFunction (data){
    if(data.status===1){
        //Return the first ancestor of the selected element: closest
        //Hide the matched elements by fading them to transparent. fadeOut
        $(mythis).closest("tr").fadeOut(1000);
            console.log("delete successfully ")
        }
        if(data.status===0){
            console.log("delete faild ")
        }

    }



// Edit or Update data

$("#Tbody").on('click','.btn-edit',function(){
    let id=$(this).attr("data-sid")
    let csf= $('input[name=csrfmiddlewaretoken]').val()
    let mydata={sid:id,csrfmiddlewaretoken:csf};
     $.ajax({
         method: "POST",
         url:'Edit_data/',
         data:mydata,
          dataType: 'json',
         success: editSuccessFunction

      });
});

    //data value  import views.py
function editSuccessFunction (data){
    // edit button a click korte id soho  create or insert a jabe
    $("#studId").val(data.id);
    $("#nameid").val(data.name);
    $("#emailid").val(data.email);
    $("#passwordid").val(data.password);
    //console.log(data)
    }