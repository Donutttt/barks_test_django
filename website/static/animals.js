fetch('/animals_data', {method: 'get'})
    .then(function(response){
        response.json().then(function(data){
            console.dir(data);
        });
    }).catch(function(err){
        console.dir(response);
    })


var AnimalComponent = React.createClass({
    render: function(){
        <div>
            <p>This is a paragraph in a react component</p>
        </div>
    }
});

console.log(document.getElementById('reactroot'));

ReactDOM.render(
    <AnimalComponent></AnimalComponent>,
    document.getElementById('reactroot')    
)

