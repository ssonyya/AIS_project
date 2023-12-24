/**
 * В данном примере адрес сервера вынесен в в отдельный js-файл с константами, 
 * также хорошей практикой считается использования переменных окружения. Это 
 * позволит на лету использовать различные настройки проекта (например, в случае, 
 * когда имеется несколько адресов для запросов: для тестирования, для продуктивного 
 * использования и т.д.)
 * Для использования переменных окружения создайте в корне проекта файл .env 
 * с содержанием, например:
 * 
 * API_URL=http://127.0.0.1:8000/api/weatherforecast
 * 
 * Значение API_URL можно получить в приложении с помощью инструкции:
 * 
 * const { API_URL } = process.env;
 */
import axios from "axios";
export const API_URL = "http://192.168.56.105:8000/api"

/**
 * Словарь доступных населённых пунктов в данном примере (для упрощения) вынесен как константа, 
 * тем не менее, было бы правильнее подгружать такие словари динамически, импользуя отдельный GET запрос к API,
 * например в методе componentDidMount().
 * Таким образом, клиентское приложение всегда будет иметь актуальные значения и соответствующие идентификаторы
 */
export const CAR_NAMES = {
}

// Интервал получения данных с сервера в мс.
export const GET_DATA_INTERVAL = 2000;
