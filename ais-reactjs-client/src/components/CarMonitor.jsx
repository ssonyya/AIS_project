import React from "react";
import axios from "axios";
import { API_URL, GET_DATA_INTERVAL } from "./constants";

/**
 * Данный компонент отображает и обновляет таблицу с 
 * данными по установленному населённому пункту 
 */

class CarMonitor extends React.Component {
    /**
     * Конструктор компонента необходима инициализировать, если в компонент передаются
     * дополнительные параметры или компонент имеет внутренние переменные хранения
     * 
     * @param {*} props - данный аргумент передает атрибуты компонента
     * 
     * this.state - атрибут класса React.Component для хранения внутренних переменных (состояний) компонента
     */
    constructor(props) {
        super(props);
        // устанавливаем состояние компонента по умолчанию
        this.state = { carData: {} , recData: {}};
    }

    /**
     * Метод getData отправляет HTTP GET запрос к серверу для получения необходимых данных.
     * 
     * В качестве HTTP-клиента для запросов вместо стандартного fetch импользуется axios.
     * Основные преимущества axios:
     * 
     * - возможность выполнения сразу нескольких HTTP-запросов;
     * - автоматическая конвертация json-данных в объект JS;
     * - поддержка сессий;
     * 
     * Для использования потребуется установка:
     * 
     * npm install axios --save
     * 
     * Подробне об особенностях axios см.: https://blog.logrocket.com/axios-vs-fetch-best-http-requests/
     */
    getData() {
        console.log('GET Request to: ' + API_URL + '/car?name=' + this.props.carName)
        // отправляем запрос на сервер, если данные получены (сервер отвечает в виде массива json-строк), 
        // обновляем массив this.state.weatherData. В случае ошибки очищаем массив. 
        axios.get(API_URL + '/car?name=' + this.props.carName)
            .then(response => {
                this.setState({
                    carData: response.data,
                }, () => { console.log(this.state) });
            }, error => {
                this.setState({
                    carData: {},
                }, () => { console.log(this.state) });
                console.log(error);
            });


        if (this.state.carData.milease < 20000){
            let data = {
                name: this.props.carName,
                status: 1,
                };
            axios.put(API_URL + '/car?name='+ data.name + '&status=' + data.status, data, {
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
        else if (this.state.carData.milease < 50000) {
            let data = {
                name: this.props.carName,
                status: 2,
                };
            axios.put(API_URL + '/car?name='+ data.name + '&status=' + data.status, data, {
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
        else if (this.state.carData.milease < 75000) {
            let data = {
                name: this.props.carName,
                status: 3,
                };
            axios.put(API_URL + '/car?name='+ data.name + '&status=' + data.status, data, {
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
        else if (this.state.carData.milease < 100000) {
            let data = {
                name: this.props.carName,
                status: 4,
                };
            axios.put(API_URL + '/car?name='+ data.name + '&status=' + data.status, data, {
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

        axios.get(API_URL + '/rectext?id=' + this.state.carData.status)
            .then(response => {
                this.setState({
                    recData: response.data,
                }, () => { console.log(this.state.carData.status) });
            }, error => {
                this.setState({
                    recData: {},
                }, () => { console.log(this.state.carData.status) });
                console.log(error);
            });
    }

    /**
     * Данный метод динамически рендерит строки таблицы, по данным, 
     * сохраненным в переменной состояния this.state.weatherData
     */
    renderData() {
        let carData = this.state.carData
        let recData = this.state.recData
        // если массив this.state.weatherData содержит данные, рендерим строки таблицы
        try{

            return (
                <tr>
                    <td>{carData.coord_x}</td>
                    <td>{carData.coord_y}</td>
                    <td>{carData.acc}</td>
                    <td>{carData.oil}</td>
                    <td>{carData.fuel}</td>
                    <td>{carData.temp}</td>
                    <td>{carData.fuel_consumption}</td>
                    <td>{carData.milease}</td>
                    <td>{recData.info}</td>
                </tr>
            );
        }
        // иначе выводим информацию об отсутствии данных
        catch(e) {
            return (
                <div className="uk-alert-danger">
                    <a className="uk-alert-close"></a>
                    <p>{e}</p>
                </div>
            )
        }
    }

    /**
     * Методы componentDidMount() и componentDidUpdate() используются для компонентов,
     * реализованных в виде классов и выполняют дополнительные действия (side effects) при
     * создании и обновлении компонента соответственно.
     * 
     * Для компонентов, реализованных в виде функций, аналогичные действия выполняет 
     * функция (хук) useEffect(). Подробнее см.: https://reactjs.org/docs/hooks-effect.html
     */

    /** 
     * Здесь метод componentDidMount() устанавливает внутренний таймер setInterval(), который 
     * выполняет метод getData() каждый 2000 мс.
     * 
     * Использование setInterval() в функциональных компонентах: 
     * https://upmostly.com/tutorials/setinterval-in-react-components-using-hooks
     */
    componentDidMount() {
        this.interval = setInterval(() => this.getData(), GET_DATA_INTERVAL);
    }

    /**
     * Таймер, созданный в компоненте необходимо также очищать при удалении компонента, 
     * для этого используется втроенная функция класса React.Component: componentWillUnmount()
     */
    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        return (
            <table className="uk-table uk-table-striped">
                <thead>
                    <tr>
                        <th>Координата Х,°</th>
                        <th>Координата У,°</th>
                        <th>Заряд аккумулятора,%</th>
                        <th>Уровень масла,%</th>
                        <th>Уровень топлива,%</th>
                        <th>Температура двигателя,°C</th>
                        <th>Расход топлива,л/100км</th>
                        <th>Пробег,км</th>
                        <th>Рекомендация</th>
                    </tr>
                </thead>
                <tbody>
                    {this.renderData()}
                </tbody>
            </table>
        );
    }
}

export default CarMonitor;