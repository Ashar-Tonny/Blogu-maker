const title = document.getElementById("id_title");
const slug = document.getElementById("id_slug");

const slugify = function (val){
    return val.toString().trim().toLowerCase()
    .replace(/&/g,'and')
    .replace(/(\s|\W|-)/g,'-')
}
title.addEventListener('keyup',(e)=>{
    slug.setAttribute('value',slugify(title.value))
})



console.log(slug.value)



