// $(document).ready(function () {
//   $('.sidenav').sidenav()
//   $('.dropdown-button').dropdown();
// })

document.addEventListener('click', dropdownMenu)

function dropdownMenu(){
  console.log('bam')
  var elems = document.querySelectorAll('.dropdown-trigger');
  var instances = M.Dropdown.init(elems, 'autoTrigger');
}