/**
 * import './App.css';
 * 
 * Стили по умолчанию App.css и index.css отключены, т.к. в данном приложении 
 * используется пакет со сторонними стилями UIKit (стили с префиксом uk-*).
 * 
 * Стили UIKit подключены через public/index.html:
 * 
 *   <link rel="stylesheet" href="%PUBLIC_URL%/uikit/css/uikit.min.css" />
 *   <script src="%PUBLIC_URL%/uikit/js/uikit.min.js"></script>
 *   <script src="%PUBLIC_URL%/uikit/js/uikit-icons.min.js"></script>
 *
 * Таким же образом можно подключать стили собственной разработки.
 * Подробнее о пакете UIKit см.: https://getuikit.com/docs/installation
 */
import React, { useState, useEffect} from "react";

import CarMonitor from "./components/CarMonitor";
import CarForm from "./components/CarForm";
import CarAdd from "./components/CarAdd";

import axios from "axios";
import { API_URL, GET_DATA_INTERVAL } from "./components/constants";




const ComboBox = ({ options,setSelectedItem,selectedItem }) => {
  const handleComboBoxChange = (event) => {
    setSelectedItem(event.target.value);
  }

  return (
    <div>
    <select onChange={handleComboBoxChange} value={selectedItem}>
      <option value="">Выберите автомобиль</option>
      {options.map((option, index) => (
        <option key={index} value={option}>{option}</option>
      ))}
    </select>
    </div>
  );
      };

/**
 * Корневой компонент App.js по умолчанию реализован в виде 
 * функционального компонента, для хранения состояния таких 
 * компонентов используется функция (хук) useState().
 * 
 * Зависимые компоненты (CityWeatherMonitor и CityWeatherForm) 
 * реализованы в виде классов и сохраняют состояние в специальном 
 * атрибуте state. Атрибут cityName={city} передаёт в данные компоненты
 * значение населённого пункта через объект props и соответствующий атрибут:
 * props.cityName
 * 
 * Подробнее о возможных реализациях React компонентов см.:
 * https://reactjs.org/docs/hooks-state.html
 * 
 */


function App() {
  var options;
  const [selectedItem, setSelectedItem] = useState('');
  const [options1, setOptions] = useState([]);
  const [isUpdCarClicked, setIsUpdCarClicked] = useState(false);

  const handleUpdCarClick = () => {
    setIsUpdCarClicked(true);
    console.log("Кнопка 'UpdCar' нажата!");
  };
  
  useEffect(() => {
    // здесь можно получить данные с сервера или из другого источника
    const fetchData = async () => {
      // например, сделаем запрос на сервер для получения списка опций
      var promise_car = axios.get(API_URL + '/carname');
      promise_car.then(promise_car => {options = promise_car.data}).then(() => setOptions(options));
    };
    fetchData();
  }, []);

  // Рендерим контент.
  // Функция map позволяет рендерить элементы массивов.
  return (
       
    <div className="uk-section uk-section-muted">

      <div>
      <ComboBox options={options1} selectedItem={selectedItem} setSelectedItem={setSelectedItem} />     
      </div>

      <div className="uk-grid uk-text-center">

      <table className="uk-table uk-table-striped">
                <thead>
                    <tr>
                        <th>Статус</th>
                        <th>Рекомендация</th>
                    </tr>
                </thead>
                <tbody>
                <tr>
                <td>1</td>
                <td>Все хорошо</td>
                </tr>
                <tr>
                <td>2</td>
                <td>Поменяйте масло</td>
                </tr>
                <tr>
                <td>3</td>
                <td>Поменяйте антифриз</td>
                </tr>
                <tr>
                <td>4</td>
                <td>Поменяйте тормозные колодки</td>
                </tr>
                </tbody>
                </table>
      <div class="marginn">
        <h2>Информация об автомобиле</h2>
      </div>

      <div className="uk-width-expand@m uk-card uk-card-default uk-card-body"><CarMonitor carName={selectedItem}/></div>
      <div className="uk-width-expand@m uk-card uk-card-default uk-card-body"><CarForm carName={selectedItem}/></div>
      

      
      <div class="marginn">
        <h2>Добавление нового авто</h2>
      </div>
      <div className="uk-width-expand@m uk-card uk-card-default uk-card-body"><CarAdd /></div>
      
      
      
      </div>
    </div>
    
  );
}

export default App;