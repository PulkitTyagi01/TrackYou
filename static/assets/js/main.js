function slideToggle(t,e,o){0===t.clientHeight?j(t,e,o,!0):j(t,e,o)}function slideUp(t,e,o){j(t,e,o)}function slideDown(t,e,o){j(t,e,o,!0)}function j(t,e,o,i){void 0===e&&(e=400),void 0===i&&(i=!1),t.style.overflow="hidden",i&&(t.style.display="block");var p,l=window.getComputedStyle(t),n=parseFloat(l.getPropertyValue("height")),a=parseFloat(l.getPropertyValue("padding-top")),s=parseFloat(l.getPropertyValue("padding-bottom")),r=parseFloat(l.getPropertyValue("margin-top")),d=parseFloat(l.getPropertyValue("margin-bottom")),g=n/e,y=a/e,m=s/e,u=r/e,h=d/e;window.requestAnimationFrame(function l(x){void 0===p&&(p=x);var f=x-p;i?(t.style.height=g*f+"px",t.style.paddingTop=y*f+"px",t.style.paddingBottom=m*f+"px",t.style.marginTop=u*f+"px",t.style.marginBottom=h*f+"px"):(t.style.height=n-g*f+"px",t.style.paddingTop=a-y*f+"px",t.style.paddingBottom=s-m*f+"px",t.style.marginTop=r-u*f+"px",t.style.marginBottom=d-h*f+"px"),f>=e?(t.style.height="",t.style.paddingTop="",t.style.paddingBottom="",t.style.marginTop="",t.style.marginBottom="",t.style.overflow="",i||(t.style.display="none"),"function"==typeof o&&o()):window.requestAnimationFrame(l)})}

let sidebarItems = document.querySelectorAll('.sidebar-item.has-sub');
for(var i = 0; i < sidebarItems.length; i++) {
    let sidebarItem = sidebarItems[i];
	sidebarItems[i].querySelector('.sidebar-link').addEventListener('click', function(e) {
        e.preventDefault();
        
        let submenu = sidebarItem.querySelector('.submenu');
        if( submenu.classList.contains('active') ) submenu.style.display = "block"

        if( submenu.style.display == "none" ) submenu.classList.add('active')
        else submenu.classList.remove('active')
        slideToggle(submenu, 300)
    })
}

window.addEventListener('DOMContentLoaded', (event) => {
    var w = window.innerWidth;
    if(w < 1200) {
        document.getElementById('sidebar').classList.remove('active');
    }
});
window.addEventListener('resize', (event) => {
    var w = window.innerWidth;
    if(w < 1200) {
        document.getElementById('sidebar').classList.remove('active');
    }else{
        document.getElementById('sidebar').classList.add('active');
    }
});

document.querySelector('.burger-btn').addEventListener('click', () => {
    document.getElementById('sidebar').classList.toggle('active');
})
document.querySelector('.sidebar-hide').addEventListener('click', () => {
    document.getElementById('sidebar').classList.toggle('active');

})


// Perfect Scrollbar Init
if(typeof PerfectScrollbar == 'function') {
    const container = document.querySelector(".sidebar-wrapper");
    const ps = new PerfectScrollbar(container, {
        wheelPropagation: false
    });
}

// Scroll into active sidebar
document.querySelector('.sidebar-item.active').scrollIntoView(false)


// for sidebar to show content on dashboard

// var endpoint = '/emp_data';

// // $(".btn_data").on('click', function (){
// $(document).on('click', ".btn", function(){   
//     var op="";
//     console.log("insideeeeeeeeeeee")
//     $.ajax({
//         method:"GET",
//         url: endpoint,
//         dataType: 'json',
//         success:function(data){
//             console.log("inside success callback")
//             viewdata(data, 'employee_details')
//             console.log(JSON.parse(data.emp_name));
//             $("#manager_teams").html("", "block");
//             // $(".table table-hover table-lg").css("display","block");
//             var emp_obj = JSON.parse(data.emp_name);
//             var emp_length = Object.keys(emp_obj).length;
            
//             for(var i=0; i<emp_length;i++){
//                 console.log(emp_obj[i]);
//                 op += '<td> <span class="emp_name">' + emp_obj[i] + ' </span> ' + emp_obj[i] + '</td>';
//                 }
//                 $('#emp_det').html(op);
                
//         },
//         error: function(error_data){
//             console.log(error_data);
//         }
//     })
//     console.log("helooooooooooooo")
    
//     function viewdata(data) {
//         document.getElementById(data);
//     }
// });

// var endpoint = '/home';
//     console.log("in the script")

//     $(document).on('click', ".btnn", function(){
//         var output="";
//         $.ajax({
//             method:"GET",
//             url: endpoint,

//             success:function(data){
//                 viewmember(data, 'manager_teams')
//                 console.log(JSON.parse(data.final_data_dict));
//             $("#employee_details".html("", "block"));

//             var mem_obj =JSON.parse(data.final_data_dict);
//             var mem_length = Object.keys(mem_obj).length;

//             for(var i=0; i<mem_length; i++){
//                 console.log(mem_obj[i]);
//                 output += '<td> <span class="final_data_dict">' + mem_obj[i] + ' </span> ' + mem_obj[i] + '</td>';
//                 }
//                 $('#member_detail').html(output);
//             },
//             error:function(error_data){
//                 console.log(error_data);
//             }
//         })
//         console.log("in the script")
//         function viewmember(data){
//             document.getElementById(data);
//         }
// });