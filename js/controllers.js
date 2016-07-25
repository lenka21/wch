var wchControllers = angular.module('wchControllers', []);

wchControllers.controller('HomeCtrl', ['$scope', '$http',
    function ($scope, $http) {
    }
]);

wchControllers.controller('AbstractCtrl', ['$scope', '$http', '$routeParams',
    function ($scope, $http, $routeParams) {
        $scope.year = $routeParams.year;

        $http.get('abstracts.json').success(function(data){
            $scope.abstracts = data['year' + $scope.year];
        });
    }
]);

wchControllers.controller('SalesCtrl', ['$scope', '$http',
    function ($scope, $http) {
        $http.get('library.json').success(function(data){
            $scope.library = data;
        });
    }
]);

wchControllers.controller('menuController', function($scope){
    $scope.menuItems = [
        {
            display: 'Abstrakty',
            children: [
                {
                    display: 'Rok 2016',
                    href: '#/abstract?year=2016'
                },
                {
                    display: 'Lata 2011-2015',
                    href: '#',
                    children: [
                        { display: '2015', href: '#/abstract?year=2015'},
                        { display: '2014', href: '#/abstract?year=2014'},
                        { display: '2013', href: '#/abstract?year=2013'},
                        { display: '2012', href: '#/abstract?year=2012'},
                        { display: '2011', href: '#/abstract?year=2011'}
                    ]
                },
                {
                    display: 'Lata 2006-2010',
                    href: '#',
                    children: [
                        { display: '2010', href: '#/abstract?year=2010'},
                        { display: '2009', href: '#/abstract?year=2009'},
                        { display: '2008', href: '#/abstract?year=2008'},
                        { display: '2007', href: '#/abstract?year=2007'},
                        { display: '2006', href: '#/abstract?year=2006'}
                    ]
                },
                {
                    display: 'Lata 2001-2005',
                    href: '#',
                    children: [
                        { display: '2005', href: '#/abstract?year=2005'},
                        { display: '2004', href: '#/abstract?year=2004'},
                        { display: '2003', href: '#/abstract?year=2003'},
                        { display: '2002', href: '#/abstract?year=2002'},
                        { display: '2001', href: '#/abstract?year=2001'}
                    ]
                },
                {
                    display: 'Lata 1996-2000',
                    href: '#',
                    children: [
                        { display: '2000', href: '#/abstract?year=2000'},
                        { display: '1999', href: '#/abstract?year=1999'},
                        { display: '1998', href: '#/abstract?year=1998'},
                        { display: '1997', href: '#/abstract?year=1997'},
                        { display: '1996', href: '#/abstract?year=1996'}
                    ]
                },
            ]
        },
    ];
});
