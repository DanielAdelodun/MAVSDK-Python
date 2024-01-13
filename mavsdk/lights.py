# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import lights_pb2, lights_pb2_grpc
from enum import Enum


class LightsResult:
    """
 

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for light requests

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         OUT_OF_BOUNDS
              Strip or Light index out of bounds

         TIMEOUT
              Request timed out

         FAILED
              Request failed

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        OUT_OF_BOUNDS = 5
        TIMEOUT = 6
        FAILED = 7

        def translate_to_rpc(self):
            if self == LightsResult.Result.UNKNOWN:
                return lights_pb2.LightsResult.RESULT_UNKNOWN
            if self == LightsResult.Result.SUCCESS:
                return lights_pb2.LightsResult.RESULT_SUCCESS
            if self == LightsResult.Result.NO_SYSTEM:
                return lights_pb2.LightsResult.RESULT_NO_SYSTEM
            if self == LightsResult.Result.CONNECTION_ERROR:
                return lights_pb2.LightsResult.RESULT_CONNECTION_ERROR
            if self == LightsResult.Result.BUSY:
                return lights_pb2.LightsResult.RESULT_BUSY
            if self == LightsResult.Result.OUT_OF_BOUNDS:
                return lights_pb2.LightsResult.RESULT_OUT_OF_BOUNDS
            if self == LightsResult.Result.TIMEOUT:
                return lights_pb2.LightsResult.RESULT_TIMEOUT
            if self == LightsResult.Result.FAILED:
                return lights_pb2.LightsResult.RESULT_FAILED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_UNKNOWN:
                return LightsResult.Result.UNKNOWN
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_SUCCESS:
                return LightsResult.Result.SUCCESS
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_NO_SYSTEM:
                return LightsResult.Result.NO_SYSTEM
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_CONNECTION_ERROR:
                return LightsResult.Result.CONNECTION_ERROR
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_BUSY:
                return LightsResult.Result.BUSY
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_OUT_OF_BOUNDS:
                return LightsResult.Result.OUT_OF_BOUNDS
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_TIMEOUT:
                return LightsResult.Result.TIMEOUT
            if rpc_enum_value == lights_pb2.LightsResult.RESULT_FAILED:
                return LightsResult.Result.FAILED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the LightsResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two LightsResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LightsResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ LightsResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"LightsResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLightsResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return LightsResult(
                
                LightsResult.Result.translate_from_rpc(rpcLightsResult.result),
                
                
                rpcLightsResult.result_str
                )

    def translate_to_rpc(self, rpcLightsResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcLightsResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcLightsResult.result_str = self.result_str
            
        
        


class LightStrip:
    """
 

     Parameters
     ----------
     lights : [uint32_t]
         
     """

    

    def __init__(
            self,
            lights):
        """ Initializes the LightStrip object """
        self.lights = lights

    def __eq__(self, to_compare):
        """ Checks if two LightStrip are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LightStrip object
            return \
                (self.lights == to_compare.lights)

        except AttributeError:
            return False

    def __str__(self):
        """ LightStrip in string representation """
        struct_repr = ", ".join([
                "lights: " + str(self.lights)
                ])

        return f"LightStrip: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLightStrip):
        """ Translates a gRPC struct to the SDK equivalent """
        return LightStrip(
                
                rpcLightStrip.lights
                )

    def translate_to_rpc(self, rpcLightStrip):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        for elem in self.lights:
          rpcLightStrip.lights.append(elem)
            
        
        


class LightMatrix:
    """
 

     Parameters
     ----------
     strips : [LightStrip]
         
     """

    

    def __init__(
            self,
            strips):
        """ Initializes the LightMatrix object """
        self.strips = strips

    def __eq__(self, to_compare):
        """ Checks if two LightMatrix are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LightMatrix object
            return \
                (self.strips == to_compare.strips)

        except AttributeError:
            return False

    def __str__(self):
        """ LightMatrix in string representation """
        struct_repr = ", ".join([
                "strips: " + str(self.strips)
                ])

        return f"LightMatrix: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLightMatrix):
        """ Translates a gRPC struct to the SDK equivalent """
        return LightMatrix(
                
                list(map(lambda elem: LightStrip.translate_from_rpc(elem), rpcLightMatrix.strips))
                )

    def translate_to_rpc(self, rpcLightMatrix):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.strips:
                
            rpc_elem = lights_pb2.LightStrip()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcLightMatrix.strips.extend(rpc_elems_list)
            
        
        



class LightsError(Exception):
    """ Raised when a LightsResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Lights(AsyncBase):
    """
 

     Generated by dcsdkgen - MAVSDK Lights API
    """

    # Plugin name
    name = "Lights"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = lights_pb2_grpc.LightsServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return LightsResult.translate_from_rpc(response.lights_result)
    

    async def set_matrix(self, matrix_colors):
        """
         Set all lights to the given colors.

         Parameters
         ----------
         matrix_colors : LightMatrix
             
         Raises
         ------
         LightsError
             If the request fails. The error contains the reason for the failure.
        """

        request = lights_pb2.SetMatrixRequest()
        
        matrix_colors.translate_to_rpc(request.matrix_colors)
                
            
        response = await self._stub.SetMatrix(request)

        
        result = self._extract_result(response)

        if result.result != LightsResult.Result.SUCCESS:
            raise LightsError(result, "set_matrix()", matrix_colors)
        

    async def set_strip(self, strip_id, strip_colors):
        """
         Set the lights on a given strip to the given colors.

         Parameters
         ----------
         strip_id : uint32_t
             
         strip_colors : LightStrip
             
         Raises
         ------
         LightsError
             If the request fails. The error contains the reason for the failure.
        """

        request = lights_pb2.SetStripRequest()
        request.strip_id = strip_id
        
        strip_colors.translate_to_rpc(request.strip_colors)
                
            
        response = await self._stub.SetStrip(request)

        
        result = self._extract_result(response)

        if result.result != LightsResult.Result.SUCCESS:
            raise LightsError(result, "set_strip()", strip_id, strip_colors)
        

    async def follow_flight_mode(self, enable):
        """
         Set whether the lights should follow the flight mode.

         Parameters
         ----------
         enable : bool
             
         Raises
         ------
         LightsError
             If the request fails. The error contains the reason for the failure.
        """

        request = lights_pb2.FollowFlightModeRequest()
        request.enable = enable
        response = await self._stub.FollowFlightMode(request)

        
        result = self._extract_result(response)

        if result.result != LightsResult.Result.SUCCESS:
            raise LightsError(result, "follow_flight_mode()", enable)
        