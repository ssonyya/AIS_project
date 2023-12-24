import React from "react";
import axios from "axios";
import { API_URL} from "./constants";

class CarAdd extends React.Component {

  constructor(props) {
    super(props);
    // устанавливаем состояние компонента по умолчанию
  
    this.state = {name: '', coord_x: '', coord_y: '', acc: '', oil: '', fuel: '', temp: '', fuel_consumption: '', milease: '', status: ''};
  }

  /**
   * Обновление данных на сервере (отправка HTTP PUT запроса).
   * 
   * Данная функция вызывается при Submit формы.
   * 
   * Конструкция updateData = (event) => {...} реализует публичную функцию, которую сразу можно
   * привязывать к событиям типа onChange, onSubmit и т.д.
   * 
   * Подробнее об обработчиках событий в компонентах React см.: https://reactjs.org/docs/handling-events.html
   * 
   * @param {*} event 
   */
  updateData = (event) => {
    console.log('POST Request to: ' + API_URL + '/car')
    // получаем Id населённого пункта из словаря и меняем состояние через встроенный метод класса React.Component setState
    // this.setState({carId: CAR_NAMES[this.props.carName]})
    event.preventDefault();   // необходимо, чтобы отключить стандартное поведение формы в браузере (AJAX)
    // формируем данные для отправки на сервер
    let data = {
      name: this.state.name,
      coord_x: parseFloat(this.state.coord_x), 
      coord_y: parseFloat(this.state.coord_y), 
      acc: parseInt(this.state.acc), 
      oil: parseInt(this.state.oil), 
      fuel: parseInt(this.state.fuel), 
      temp: parseFloat(this.state.temp),  
      fuel_consumption: parseFloat(this.state.fuel_consumption), 
      milease: parseInt(this.state.milease), 
      status: parseInt(this.state.status)
    };
    // HTTP-клиент axios автоматически преобразует объект data в json-строку
    axios.post(API_URL + '/car', data, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json;charset=UTF-8",
      },
    })
    .then(response => {
      console.log('Response: ' + response.status);
    }, error => {
        console.log(error);
        alert(error);
    });
  }

  render() {
    return (
      <form onSubmit={this.updateData} className="uk-form-stacked">
      <div>
      <table className="uk-table uk-table-striped" border="1">
                <thead>
                    <tr>
                        <th>Регномер</th>
                        <th>Координата Х,°</th>
                        <th>Координата У,°</th>
                        <th>Заряд аккумулятора,%</th>
                        <th>Уровень масла,%</th>
                        <th>Уровень топлива,%</th>
                        <th>Температура двигателя,°C</th>
                        <th>Расход топлива,л/100км</th>
                        <th>Пробег,км</th>
                        <th>Статус</th>
                    </tr>
                </thead>
                <tr>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({name: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({coord_x: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({coord_y: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({acc: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({oil: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({fuel: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({temp: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({fuel_consumption: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({milease: e.target.value})}} /></td>
                <td><input type="text" class="inputtable" onChange={(e) => {this.setState({status: e.target.value})}} /></td>
                </tr>
      </table>
      <input type="submit" value="Добавить" className="btnn-new"/>
      </div>  
      </form>  
    );
  }

}

export default CarAdd;