import React from "react";
import axios from "axios";
import { API_URL} from "./constants";

class CarForm extends React.Component {

  constructor(props) {
    super(props);
    // устанавливаем состояние компонента по умолчанию
  
    this.state = {name: '', status: ''};
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
    console.log('PUT Request to: ' + API_URL + '/car?name='+ this.props.carName + '&status=' + this.state.status)
    // получаем Id населённого пункта из словаря и меняем состояние через встроенный метод класса React.Component setState
    // this.setState({carId: CAR_NAMES[this.props.carName]})
    event.preventDefault();   // необходимо, чтобы отключить стандартное поведение формы в браузере (AJAX)
    // формируем данные для отправки на сервер
    let data = {
      name: parseFloat(this.state.name), 
      status: parseInt(this.state.status), 
    };
    // HTTP-клиент axios автоматически преобразует объект data в json-строку
    axios.put(API_URL + '/car?name='+ this.props.carName + '&status=' + this.state.status, data, {
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
        <div class="marginn">
          <h2>Обновление статуса автомобиля</h2>
        </div>
        <div>
          <label>Введите статус автомобиля</label>
          <input type="text" onChange={(e) => {this.setState({status: e.target.value})}} />
          <input type="submit" value="Обновить" className="btnn-new"/>
        </div>
      </form>
    );
  }

}

export default CarForm;