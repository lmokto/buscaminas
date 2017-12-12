var generate_data = function(){
    data = {}
    for(var y = 1; y < clm+1; y++){
        data[y] = []
        for(var x = 1; x < row+1; x++) {
            data[y][x] = []
            data[y][x]['mine'] = false
            data[y][x]['number'] = false
            data[y][x]['space'] = false
        }
    }
    return data;
}

var assigned_values = function(data, assgined, type){
    for(var y = 0; y < clm+1; y++){
        if (assgined[y]){
            assgined[y].forEach(function(a, b, c){
                for(var x = 1; x < row+1; x++) {
                    if (a.hasOwnProperty(x)){
                        if (type == 'mines'){
                            data[y][x]['mine'] = true
                        } else if (type == 'spaces'){
                            data[y][x]['space'] = true
                        } else if (type == 'numbers'){
                            data[y][x]['number'] = a[x]
                        }
                    }
                }
            });
        }
    }
    return data;
}


angular.module('app', [])
   .controller('buscaminaCtrl', function($scope, $http) {

        $scope.title = "Buscaminas";
        $scope.data = null;
        click = 0;

        $scope.setFlagSign = function(type, value, event){
            $(event.target)[0].textContent = "?";
        }

        $scope.changeValue = function(type, value, event){

            if(click == 0){
                $scope.start_game = new Date().toUTCString();
                start_timestamp = Math.floor($scope.start_game / 1000);
                console.log("start", $scope.start_game);
            }

            if (value == 'mine' && type == true){
                alert('Perdiste');
                $(event.target)[0].textContent= "BOOM";
                $scope.end_game = new Date().toUTCString();
                end_timestamp = Math.floor($scope.end_game / 1000);
                console.log("start", $scope.end_game);
            } else if (value == 'space'){
                $(event.target)[0].textContent = "SPACE"
            } else if (value == 'number'){
                $(event.target)[0].textContent= type
            }

            click += 1

        }

        $http.get('http://127.0.0.1:5000/api/generate/beginner')
        .then(function (success){

            $scope.dimension = success.data.dimension;

            clm =  $scope.dimension.clm;
            row =  $scope.dimension.row;

            data = generate_data()
            assigned_values(data, success.data.mines, 'mines')
            assigned_values(data, success.data.numbers, 'numbers')
            assigned_values(data, success.data.spaces, 'spaces')

            $scope.data = data;
            console.log(data)

        },function (error){
            console.log(error)
        });
   }

).directive('ngRightClick', function($parse) {
    return function(scope, element, attrs) {
        var fn = $parse(attrs.ngRightClick);
        element.bind('contextmenu', function(event) {
            scope.$apply(function() {
                event.preventDefault();
                fn(scope, {$event:event});
            });
        });
    };
});
