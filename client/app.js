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
            console.log(success.data);
            $scope.data = {}
            for(var y = 1; y < $scope.dimension.clm+1; y++){
                $scope.data[y] = []
                mines = $scope.mines[y]
                numbers = $scope.numbers[y]
                spaces = $scope.spaces[y]
                for(var x = 1; x < $scope.dimension.row+1; x++) {
                    x_mine = mines[x]
                    x_number = numbers[x]
                    x_space = spaces[x]
                    debugger;
                    if (true){
                        $scope.data[y].push({'mine':true,'number':null,'space':null})
                    } else if (true){
                        $scope.data[y].push({'mine':null,'number':1,'space':null})
                    } else if (true){
                        $scope.data[y].push({'mine':null,'number':null,'space':true})
                    }
                }
            }
            console.log($scope.data)
        },function (error){
            console.log(error)
        });
   }
);