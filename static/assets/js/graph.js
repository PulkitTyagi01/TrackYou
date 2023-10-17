// buttondropdown function start
console.log('checkdev');
jQuery('.graph_dropdown_btn li button').click(function(){
	var test = jQuery(this).attr('data-tab');
    jQuery('.graph_div').removeClass('active')
	jQuery('#' + test).addClass('active');

})
// for refresh the page
$('#myModal').on('hidden.bs.modal', function () {
 location.reload();
})
// buttondropdown function end
//name1='Pulkit'

$(".EmployeeGraph").click(function() {
    var $div = $(this).closest("div");    // Find the row
    var $text = $div.find(".username").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)

    var endpoint = "/graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});
var myCharts;


$(".EmployeeGraph").click(function() {
    var $div = $(this).closest("div");    // Find the row
    var $text = $div.find(".username").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/graph_data/" + name1,
        data: { 
            // "by_days": by_days
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraphWithDetails(response, 'myChartBarDays');
        },
        error: function(response) {
            console.log('error');
        }
    });
});
var myChart;



$(".EmployeeGraph").click(function() {
    var $div = $(this).closest("div");    // Find the row
    var $text = $div.find(".username").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/graph_data/" + name1,
        data: { 
            // "by_months": by_months
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');
            MonthsGraph(response, 'myChartBarMonths');
        },
        error: function(response) {
            console.log('error');
        }
    });
});

var myChart1


$(".TeamEmployeeGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)

    var endpoint = "/graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});
var myCharts;



$(".TeamEmployeeGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/graph_data/" + name1,
        data: { 
            // "by_days": by_days
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraphWithDetails(response, 'myChartBarDays');
        },
        error: function(response) {
            console.log('error');
        }
    });
});
var myChart;



$(".TeamEmployeeGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/graph_data/" + name1,
        data: { 
            // "by_months": by_months
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');
            MonthsGraph(response, 'myChartBarMonths');
        },
        error: function(response) {
            console.log('error');
        }
    });
});

var myChart1

$(".ProjectGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)

    var endpoint = "/project_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');


        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});
var myCharts;


$(".ProjectGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/project_graph_data/" + name1,
        data: { 
            // "by_days": by_days
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraph(response, 'myChartBarDays');
        },
        error: function(response) {
            console.log('error');
        }
    });
});
var myChart;


$(".ProjectGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/project_graph_data/" + name1,
        data: { 
            // "by_months": by_months
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');
            MonthsGraph(response, 'myChartBarMonths');
        },
        error: function(response) {
            console.log('error');
        }
    });
});

var myChart1


$(".TeamGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)

    var endpoint = "/team_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');


        },
        // on error
        error: function(response) {
            console.log('error');
            border-bottom
        }
    });
});
var myCharts;


$(".TeamGraph").click(function() {
    var $row = $(this).closest("tr");
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")    // Find the rowborder-bottom
    $.ajax({
        type: "GET",
        url:  "/team_graph_data/" + name1,
        data: { 
            // "by_days": by_days
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraph(response, 'myChartBarDays');
        },
        error: function(response) {
            console.log('error');
        }
    });
});
var myChart;



$(".TeamGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-3").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/team_graph_data/" + name1,
        data: { 
            // "by_months": by_months
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');

            MonthsGraph(response, 'myChartBarMonths');
        },
        error: function(response) {
            console.log('error');
        }
    });
});

var myChart1

$(".ProjectListGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-abc").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)

    var endpoint = "/project_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');


        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});
var myCharts;


$(".ProjectListGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-abc").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/project_graph_data/" + name1,
        data: { 
            // "by_days": by_days
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraph(response, 'myChartBarDays');
        },
        error: function(response) {
            console.log('error');
        }
    });
});
var myChart;



$(".ProjectListGraph").click(function() {
    var $row = $(this).closest("tr");    // Find the row
    var $text = $row.find(".col-abc").text(); // Find the text
    var name1 = $text.replace(/\s+/g,"")
    
    // Let's test it out
    console.log(name1)


    $.ajax({
        type: "GET",
        url:  "/project_graph_data/" + name1,
        data: { 
            // "by_months": by_months
        },
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');

            MonthsGraph(response, 'myChartBarMonths');
        },
        error: function(response) {
            console.log('error');
        }
    });
});

var myChart1


$(".graph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myCharts;

$(".graph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraphWithDetails(response, 'myChartBarDays');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myChart;

$(".graph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');

            MonthsGraph(response, 'myChartBarMonths');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myChart1;

$(".teamgraph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/team_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myCharts;

$(".teamgraph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/team_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraph(response, 'myChartBarDays');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myChart;

$(".teamgraph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/team_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');

            MonthsGraph(response, 'myChartBarMonths');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myChart1;

$(".projectgraph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/project_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('---------------start');
            WeeksGraph(response, 'myChartBarWeeks');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myCharts;

$(".projectgraph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/project_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_DAYS');
            DaysGraph(response, 'myChartBarDays');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myChart;

$(".projectgraph").click(function() {
    //var test1=document.getElementById('search_div')
    var test=document.getElementById('li0')
    console.log(test.textContent)
    //var $row = $(this).closest("tr");    // Find the row
    //var $text = $row.find(".filter_search_label").text(); // Find the text
    var name = test.textContent
    var name1 = name.replace(/\s+/g,"")
    console.log('Hai1')
    // Let's test it out
    console.log(name1)

    var endpoint = "/project_graph_data/" + name1
    $.ajax({
        type: 'GET',
        data: {
            // "by_weeks": by_weeks,
            // "hours": hours,
        },
        url: endpoint,
        dataType: "json",
        success: function(response) {
            console.log('start ===============>>>>>>>>>>>> BY_Months');

            MonthsGraph(response, 'myChartBarMonths');
        },
        // on error
        error: function(response) {
            console.log('error');
            
        }
    });
});

var myChart1;



function DaysGraph(data, a) {
    var graph = data['by_days'];
    const by_days = [];
    const hours = [];

    for (let k in graph) {
        by_days.push(k);
        hours.push(graph[k]);
    }
    var by_months = data.by_months;    
    var by_weeks = data.by_weeks;
    var ctx = document.getElementById(a).getContext('2d');
    
    if (myChart) myChart.destroy();

    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: by_days,
            datasets: [{
                data: hours,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(301, 120, 245, 0.2)',
                    'rgba(0, 102, 153, 0.2)',
                    'rgba(255, 120, 130, 0.2)',
                    'rgba(153, 102, 215, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(200, 99, 130, 1)',
                    'rgba(255, 19, 130, 1)',
                    'rgba(255, 90, 100, 1)',
                    'rgba(255, 159, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Hours'
                      }

                }],
                xAxes: [{
                    ticks: {
                        autoSkip : false,
                        min: 0, // it is for ignoring negative step.
                        beginAtZero: true,
                        padding: 0.5,
                        stepSize: 0.5 // if i use this it always set it '1', which look very awkward if it have high value  e.g. '100'.
                    },
                    barPercentage: 0.4
                }]
            },
            legend: {
                display: false //This will do the task
            },
            responsive: true,
        }

    });
    addEventListener('click', function(evt) {
        console.log("----------------------")
        var firstPoint = myChart.getElementAtEvent(evt)[0];
        if (firstPoint) {
            var label = myChart.data.labels[firstPoint._index];
            var value = myChart.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
            alert('Date : ' + label + "\nHours : " + value );
        }
    });
    // myChart.clear();
    
}


function DaysGraphWithDetails(data, a) {
    var graph = data['by_days'];
    var details = data['daily_report_daywise']
    const by_days = [];
    const hours = [];
    const description = [];


    for (let k in graph) {
        by_days.push(k);
        hours.push(graph[k]);
    }
    for (let l in details) {
        description.push(details[l])
    }
    var by_months = data.by_months;    
    var by_weeks = data.by_weeks;
    var ctx = document.getElementById(a).getContext('2d');
    
    if (myChart) myChart.destroy();

    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: by_days,
            details: description,
            datasets: [{
                data: hours,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(301, 120, 245, 0.2)',
                    'rgba(0, 102, 153, 0.2)',
                    'rgba(255, 120, 130, 0.2)',
                    'rgba(153, 102, 215, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(200, 99, 130, 1)',
                    'rgba(255, 19, 130, 1)',
                    'rgba(255, 90, 100, 1)',
                    'rgba(255, 159, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Hours'
                      }

                }],
                xAxes: [{
                    ticks: {
                        autoSkip : false,
                        min: 0, // it is for ignoring negative step.
                        beginAtZero: true,
                        padding: 0.5,
                        stepSize: 0.5 // if i use this it always set it '1', which look very awkward if it have high value  e.g. '100'.
                    },
                    barPercentage: 0.4
                }]
            },
            legend: {
                display: false //This will do the task
            },
            responsive: true,
        }

    });
    
    addEventListener('click', function(evt) {
        console.log("check first")
        var firstPoint = myChart.getElementAtEvent(evt)[0];
        if (firstPoint) {
            var label = myChart.data.labels[firstPoint._index];
            var value = myChart.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
            var details = myChart.data.details[firstPoint._index];
            alert('Date : ' + label + "\nHours : " + value + '\nDetails :' + details);
        }
    });
    // myChart.clear();
    
}




function WeeksGraph(data, b) {

    var something = data['by_weeks'];
    const by_weeks = [];
    const hours = [];
    
    
    for (let k in something) {
        by_weeks.push(k);
        hours.push(something[k]);
    }
    var by_months = data.by_months;    
    var by_days = data.by_days;
    var ctx = document.getElementById(b).getContext('2d');
    // myCharts.destroy();
    if (myCharts) myCharts.destroy();
    myCharts = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: by_weeks,
            datasets: [{
                data: hours,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(0, 102, 153, 0.2)',
                    'rgba(255, 120, 130, 0.2)',
                    'rgba(153, 102, 215, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(200, 99, 130, 1)',
                    'rgba(255, 19, 130, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }],
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Hours'
                      }

                }],
                xAxes: [{
                    ticks: {
                        autoSkip : false,
                        min: 0, // it is for ignoring negative step.
                        beginAtZero: true,
                        padding: 0.5,
                        stepSize: 0.5 // if i use this it always set it '1', which look very awkward if it have high value  e.g. '100'.
                    },
                    barPercentage: 0.4
                }]
            },
            legend: {
                display: false //This will do the task
            },
            responsive: true,
        },
    });
    // myCharts.update();
    // myCharts.clear();

    addEventListener('click', function(evt) {
        console.log("----------------------")
        var firstPoint = myCharts.getElementAtEvent(evt)[0];
        if (firstPoint) {
          var label = myCharts.data.labels[firstPoint._index];
          var value = myCharts.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
      
          alert('Week : ' + label + "\nHours : " + value);
        }
    });

}

function MonthsGraph(data, c) {
    var graph = data['by_months'];
    const by_months = [];
    const hours = [];


    for (let k in graph) {
        by_months.push(k);
        hours.push(graph[k]); 
    }
    var by_days = data.by_days;    
    var by_weeks = data.by_weeks;
    var ctx = document.getElementById(c).getContext('2d');
    if (myChart1) myChart1.destroy();

    myChart1 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: by_months,
            datasets: [{
                data: hours,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(0, 102, 153, 0.2)',
                    'rgba(255, 120, 130, 0.2)',
                    'rgba(153, 102, 215, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(200, 99, 130, 1)',
                    'rgba(255, 19, 130, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Hours'
                      }

                }],
                xAxes: [{
                    ticks: {
                        autoSkip : false,
                        min: 0, // it is for ignoring negative step.
                        beginAtZero: true,
                        padding: 0.5,
                        stepSize: 0.5 // if i use this it always set it '1', which look very awkward if it have high value  e.g. '100'.
                    },
                    barPercentage: 0.4
                }]
            },
            legend: {
                display: false //This will do the task
            },
            responsive: true,
        }
    });
    addEventListener('click', function(evt) {
        console.log("---------------second-------")
        var firstPoint = myChart1.getElementAtEvent(evt)[0];
        if (firstPoint) {
          var label = myChart1.data.labels[firstPoint._index];
          var value = myChart1.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
      
          alert('Month : ' + label + "\nHours : " + value);
        }
    });
}




// var data = {
//     labels: ['January', 'February', 'March'],
    
//     datasets: [
//         {
//         fillColor: "rgba(220,220,220,0.2)",
//         strokeColor: "rgba(220,220,220,1)",
//         pointColor: "rgba(220,220,220,1)",
//         pointStrokeColor: "#fff",
//         pointHighlightFill: "#fff",
//         pointHighlightStroke: "rgba(220,220,220,1)",
//         data: [30,120,90]
//         },
//         {
//         fillColor: "rgba(100,220,220,0.7)",
//         strokeColor: "rgba(220,220,220,1)",
//         pointColor: "rgba(220,220,220,1)",
//         pointStrokeColor: "#fff",
//         pointHighlightFill: "#fff",
//         pointHighlightStroke: "rgba(220,220,220,1)",
//         data: [10,70,110]
//         }
//     ]
//     };

//     var context = document.querySelector('#myChartBar').getContext('2d');
//     new Chart(context).bar(data);
