
var AnimalComponent = React.createClass({
    render: function(){


        console.log(this.props.animalInput.image);

        var animalImage = this.props.animalInput.image !== "image" ? 
                (
                    <img className="animal-listing-image" src={"/media/" + this.props.animalInput.image} />
                )
                :
                (
                    <div className="animal-listing-image-placeholder"></div>
                );


        return (
            <div className="animal-listing row">
                 <div className="animal-type-div">
                    <span className="animal-type">{ this.props.animalInput.type }</span>
                </div>
                <div className="animal-listing-image-wrapper col-xs-12 col-sm-4">
                    {animalImage}
                </div>
                <div className="animal-listing-description col-xs-12 col-sm-8">
                    <h4>{ this.props.animalInput.name }</h4>
                    <div className="description-wrapper">
                        <p>{ this.props.animalInput.description }</p>
                    </div>
                </div>
            </div>
        )
    }
});

var AnimalListing = React.createClass({
    getInitialState(){
        return {
            allAnimals: [],
            filteredAnimals: [],
            selectedAnimalType: "",
            animalTypes: [],
        }   
    },

    /*sets the animals state to the provided value*/
    setAnimals(newAnimals){
        this.setState({allAnimals: newAnimals})
        this.setAnimalTypes();
        this.setFilteredAnimals();
    },

    /*add in a single animal (not yet tested)*/
    addAnimal(newAnimal){
        var withAdditionalAnimal = [
            ...this.state.allAnimals,
            newAnimal
        ];
        this.setState({allAnimals: withAdditionalAnimal});
    },

    /*loads in animal data*/
    loadAnimals(){
        var self = this;
        fetch('/animals_data', {method: 'get'})
            .then(function(response){
                response.json()
                    .then(function(data){
                        self.setAnimals(data);
                    });
            }).catch(function(err){
                console.dir(response);
            })

       
    },

    /*sets the animals which match the current filters*/
    setFilteredAnimals(){
        var self = this;
        var updatedFilteredAnimals = this.state.allAnimals.filter(function(animal, index){
            var doesMatch = self.state.selectedAnimalType !== "" ? animal.type === self.state.selectedAnimalType : true;
            console.log(animal.type + ' ' + self.state.selectedAnimalType);
            return doesMatch; 
        });

        self.setState({ filteredAnimals: updatedFilteredAnimals });
    },

    /*sets the types of animals for the currently selected animals*/
    setAnimalTypes(){
        var self = this;
        var newAnimalTypes = [];

        for (var i = 0; i < this.state.allAnimals.length; i++){
            var currAnimalType = this.state.allAnimals[i].type;
            if (newAnimalTypes.indexOf(currAnimalType) === -1){
                newAnimalTypes.push(currAnimalType);
            }
        }
        self.setState({ animalTypes: newAnimalTypes });
    },
    
    /*hook after component is mounted*/
    componentDidMount(){
        this.loadAnimals();
    },

    selectedAnimalChange(event){
        //we pass the set filtered animals as a callback because state is not updated immediately
        this.setState({ selectedAnimalType: event.target.value }, function(){
            this.setFilteredAnimals();
        }); 
    },

    render(){
        return (
            <div className="animal-list-wrapper">
                <div className="filter-wrapper">
                    <select onChange={this.selectedAnimalChange} value={this.state.selectedAnimalType}>
                        <option value="">Show all</option>
                        {
                            this.state.animalTypes.map(function(type, index){
                                return <option key={index}>{type}</option>
                            })
                        }
                    </select>
                </div>
                <div className="animal-list">
                    {
                        this.state.filteredAnimals.map(function(animal, index){
                            return <AnimalComponent key={index} animalInput={animal}></AnimalComponent>;
                        })
                    }
                </div>
            </div>
        )
    },
});

console.log(document.getElementById('reactroot'));

ReactDOM.render(
    <AnimalListing></AnimalListing>,
    document.getElementById('reactroot')    
)

