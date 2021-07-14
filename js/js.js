 
var img=document.forms['myform']['img_upload'];
var valid=["png","jpg","jpeg"];
function validation() {

  if(img.value!='')
  {
    var pos_of_dot= img.value.lastIndexOf('.')+1;
    var img_ext= img.value.substring(pos_of_dot);

    var result= valid.includes(img_ext);

    if(result==false)
    {
      alert("Allowed image types are - png, jpg, jpeg");
      return false;
    }
    else 
     {
      if(parseFloat(img.files[0].size/(1024*1024))>=3)
      {
        alert("File size must be Smaller than 3 MB")
        return false;
      }
    }
  }
  else{
    alert("No image is Selected...");
    return false;
  }
return true;
}
