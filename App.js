import 'react-native-reanimated';
import {AppRegistry,} from "react-native";
import app from './app.json';
import AppNav from "./navigations/AppNav";
import {NavigationContainer} from "@react-navigation/native";
import {BasketProvider} from "./context/BasketContext";

const App = function () {
    return (
        <BasketProvider>
            <NavigationContainer>
                <AppNav />
            </NavigationContainer>
        </BasketProvider>
    )
}


export default App;
AppRegistry.registerComponent(app.expo.name, () => App);