$(document).on("click", ".open-dtlDialog", function () {
                 var myMonth = $(this).data('month');
                 var billType = $(this).data('type');
                 var dateposted = $(this).data('posteddate');
                 var datepaid = $(this).data('paiddate');
                 var amountDue = $(this).data('amountd');
                 if(billType == "Water") {
                        document.getElementById('headerlogo').src ='img/fish.png';
                        // code to be executed if condition is true
                    } 
                 else {
                    if(billType == "Rent") {
                        document.getElementById('headerlogo').src ="{% static 'img/house.jpg' %}";
                        // code to be executed if condition is true
                    }
                    if(billType == "Electricity") {
                        document.getElementById('headerlogo').src ="{% static 'img/electric.png' %}";
                        // code to be executed if condition is true
                    }

                 }
                 $(".modal-body #month").val( myMonth );
                 $(".modal-header #billMonth").text(billType + ' Bill for ' + myMonth );
                 $(".modal-body #postedDate").text( dateposted );
                 $(".modal-body #paidDate").text( datepaid );
                 $(".modal-body #amountDue").text( amountDue );
                 // As pointed out in comments, 
                 // it is superfluous to have to manually call the modal.
                 // $('#addBookDialog').modal('show');
            });