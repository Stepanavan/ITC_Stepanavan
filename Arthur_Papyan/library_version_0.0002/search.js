
var app = angular.module("app", []);



app.filter('searchFor', function(){


	return function(arr, searchString){

        // return all arry
		if(!searchString){
			return ;
		}

		var result = []; 
        
        
        //convert to lower case  
		searchString = searchString.toLowerCase();

        //
		angular.forEach(arr, function(item){
          
            

			if(item.title.toLowerCase().indexOf(searchString) !== -1){
				result.push(item);

			}
			if(item.category.toLowerCase().indexOf(searchString) !== -1){
				result.push(item);

			}

		});

		return result;
	};

});



function Ctrl($scope){

	$scope.books = [
		{
			url: 'books/01.html',
			title: 'Преступление и наказание',
			author: 'Достоевский, Михаил Михайлович',
			rating: 5,
			category:"romance",
			image: 'image/books/prenak.jpg',
			exist:true,
			
		},
				{
			url: 'books/02.html',
			title: '451° по Фаренгейту',
			author: 'Рей Брэдбери',
			rating: 5,
			category:"phantasy",
			image: 'image/books/451.jpg',
			exist:true,
		
		},
				{
			url: 'books/03.html',
			title: 'Мастер и Маргарита',
			author: 'Михаил Афанасьевич Булгаков',
			rating: 5,
			category:"phantasy",
			image: 'image/books/masterimargarita.jpg',
			exist:false,
		
		}
	
	];
	
	$scope.display_limit = 8;
  	$scope.users = [];
  	(function () {
    	for (var i = 0; i < $scope.books.length; i++) {
      		$scope.books[i].name=i;
		}
  	})()
	
	
	console.log($scope.books)
	
	
}	




app.directive('scrollPosition', function ($window) {
  return function (scope, element, attrs) {      
    var w = element[0];
    //var w = $window;
    angular.element(w).bind('scroll', function () {                  
      scope.$apply(function () {                
        if (w.scrollTop + w.offsetHeight >= w.scrollHeight) {          
          scope.display_limit = scope.display_limit + 8;
        }
      });
    });
  }
});

