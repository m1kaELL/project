var basket = [];

$(document).ready(function () {
    var form = $('#form_review_film');
    console.log(basket);
    console.log(localStorage.getItem("basket"))
    if (basket.length == 0) {
        $(".review-items").addClass("visibility-hidden");
    }
    if (localStorage.getItem("basket")) {
        basket = JSON.parse(localStorage.getItem("basket"))
        drawBasket()
        //addButtonBuy()
    }
   

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
        var review = $("#review").val();
        console.log(review);
        var submit_btn = $("#submit_btn");
        var film_id = submit_btn.data("film_id");
        var film_name = submit_btn.data("film_name");
        console.log(film_id);
        console.log(film_name);

        var newItem = true

        if (newItem) {
            basket.push({
                id: film_id,
                name: film_name,
                review: review
            })

        }
        localStorage.setItem("basket", JSON.stringify(basket))
        console.log(basket)
        drawBasket()
        //review_Updating(film_id,number,is_delete=false);
        
    
    })
    function drawBasket() {
        $(".review-items").html("")
        basket.forEach((itemInBasket, index) => {
            if (itemInBasket) {
                $(".review-items").removeClass("visibility-hidden");
                $(".review-items").append('<li class="font-style-Arial">' + itemInBasket.name +
                    '<br><input class = "form-input-type-text product_number" type="text" maxlength = "5" value =' + itemInBasket.review + ' disabled>' +
                    '<a class= "delete-item" href="" data-basket_index="' + index + '"> x</a>' + '</li>');
            }

        })
        $("#review_total_number").text("(" + basket.length + ")")


    } 

    function showingReview(){
        $('.review-items').toggleClass("d-none");

    }

    $(".my_basket").on("click",function(e){
        e.preventDefault();
        showingReview();
    })
    $(document).on("click", ".delete-item", function(e){
        e.preventDefault();
        basket_index = $(this).data("basket_index");
        console.log(basket_index);
        basket.splice(basket_index, 1);
        if (basket.length == 0) {
            $(".review-items").addClass("visibility-hidden");
        }
        drawBasket()
        localStorage.setItem("basket", JSON.stringify(basket))

    })
})