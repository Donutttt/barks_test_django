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
        return (
            <div>
                <p>This is a paragraph in a react component</p>
            </div>
        )
    }
});

var AnimalListing = React.createClass({
    getInitialState(){
        return {
            animals: [],
            filters: [],    
        }   
    },

    /*sets the animals state to the provided value*/
    setAnimals(newAnimals){
        this.setState({animals: newAnimals})
    },

    /*add in a single animal (not yet tested)*/
    addAnimal(newAnimal){
        var withAdditionalAnimal = [
            ...this.state.animals,
            newAnimal
        ];
        this.setState({animals: withAdditionalAnimal});
    },

    /*loads in animal data*/
    loadAnimals(){
        var self = this;
        fetch('/animals_data', {method: 'get'})
            .then(function(response){
                response.json()
                    .then(function(data){
                        self.setAnimals(data);
                        console.log(self.state.animals);
                    });
            }).catch(function(err){
                console.dir(response);
            })

       
    },
    
    /*hook after component is mounted*/
    componentDidMount(){
        this.loadAnimals();    
    },

    render(){
        return (
            <div>
                {
                    this.state.animals.map(function(animal, index){
                        return <p key={index}>{animal.name}</p>;
                    })
                }
            </div>
        )
    },
});

console.log(document.getElementById('reactroot'));

ReactDOM.render(
    <AnimalListing></AnimalListing>,
    document.getElementById('reactroot')    
)

