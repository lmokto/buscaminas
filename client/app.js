angular.module('app', [])
   .controller('buscaminaCtrl', function($scope, $http) {
        $scope.title = "Buscaminas";
        $scope.data = null;
        $http.get('http://127.0.0.1:5000/api/generate/beginner')
        .then(function (success){
            $scope.mines = success.data.mines;
            $scope.numbers = success.data.numbers;
            $scope.spaces = success.data.spaces;
            $scope.dimension = success.data.dimension;
        },function (error){
            console.log(error)
        });
   }
);