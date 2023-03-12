class ResponseDTO:
    def __init__(
            self,
            success: bool,
            status_code: int,
            message: str = None,
            result: [dict, list[dict], str] = None,
    ):
        self.__success = success
        self.__status_code = status_code
        self.__message = message
        self.__result = result

    def get_response_dto(self):
        response = {
            "success": self.__success,
            "status_code": self.__status_code,
            "message": self.__message,
            "result": self.__result,
        }

        return response
