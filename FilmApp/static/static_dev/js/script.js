$(document).ready(function(){
    var form = $('#form_review_film');
    console.log(form);

    function review_Updating(film_id,number,is_delete){

        var data = {};
        data.film_id=film_id;
        data.number=number;
        var csrf_token= $('#form_review_film [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        if (is_delete){
            data["is_delete"]=true;
        }

        var url = form.attr("action");

        console.log(data);
        
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.total_review);

                if (data.total_review || data.total_review == 0){
                    $("#total_review").text("("+data.total_review+")");
                    console.log(data.films);
                   //$(".review-items ul").html("");
                    $.each(data.film,function(k,value){
                        $(".review-items ul").append("<li>"+value.film_name+
                        '<a class="delete-item" href="" data-film_id = "" + value.id +> x <a>'+
                        "</li>");



                    })
                }

                    },
                    error:function(){
                        console.log("error");
                    }
                
            
        })

    }

    form.on("submit" , function(e){
        e.preventDefault();
        console.log('123');

        var number = $("#review").val();
        console.log(number);
        var submit_btn = $("#submit_btn");
        var film_id = submit_btn.data("film_id");
        var film_name = submit_btn.data("film_name");
        console.log(film_id);
        console.log(film_name);

       

        
        review_Updating(film_id,number,is_delete=false);
        
    
    })

    function showingReview(){
        $('.review-items').removeClass("d-none");

    }

    $(".review-container").on("click",function(e){
        e.preventDefault();
        showingReview();
    })
    $(".review-container").mouseover(function(){
        showingReview();
    })

    $(".review-container").mouseout(function(){
        $('.review-items').addClass("d-none");
    })
    $(document).on("click", ".delete-item", function(e){
        e.preventDefault();
        /* $(this).closest("li").remove();*/
        film_id=$(this).data("film_id");
        number = 0;
        review_Updating(film_id,number,is_delete=true);

    })
})