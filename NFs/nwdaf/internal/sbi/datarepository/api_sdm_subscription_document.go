/*
 * Nnwdaf_DataRepository API OpenAPI file
 *
 * Unified Data Repository Service
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package datarepository

import (
// "net/http"
//
// "github.com/gin-gonic/gin"
//
// "github.com/free5gc/nwdaf/internal/logger"
// "github.com/free5gc/nwdaf/internal/sbi/producer"
// "github.com/enable-intelligent-and-containerized-5g/openapi"
// "github.com/enable-intelligent-and-containerized-5g/openapi/models"
// "github.com/free5gc/util/httpwrapper"
)

// HTTPRemovesdmSubscriptions - Deletes a sdmsubscriptions
// func HTTPRemovesdmSubscriptions(c *gin.Context) {
// 	req := httpwrapper.NewRequest(c.Request, nil)
// 	req.Params["ueId"] = c.Params.ByName("ueId")
// 	req.Params["subsId"] = c.Params.ByName("subsId")
//
// 	rsp := producer.HandleRemovesdmSubscriptions(req)
//
// 	responseBody, err := openapi.Serialize(rsp.Body, "application/json")
// 	if err != nil {
// 		logger.DataRepoLog.Errorln(err)
// 		problemDetails := models.ProblemDetails{
// 			Status: http.StatusInternalServerError,
// 			Cause:  "SYSTEM_FAILURE",
// 			Detail: err.Error(),
// 		}
// 		c.JSON(http.StatusInternalServerError, problemDetails)
// 	} else {
// 		c.Data(rsp.Status, "application/json", responseBody)
// 	}
// }

// HTTPUpdatesdmsubscriptions - Stores an individual sdm subscriptions of a UE
// func HTTPUpdatesdmsubscriptions(c *gin.Context) {
// 	var sdmSubscription models.SdmSubscription
//
// 	requestBody, err := c.GetRawData()
// 	if err != nil {
// 		problemDetail := models.ProblemDetails{
// 			Title:  "System failure",
// 			Status: http.StatusInternalServerError,
// 			Detail: err.Error(),
// 			Cause:  "SYSTEM_FAILURE",
// 		}
// 		logger.DataRepoLog.Errorf("Get Request Body error: %+v", err)
// 		c.JSON(http.StatusInternalServerError, problemDetail)
// 		return
// 	}
//
// 	err = openapi.Deserialize(&sdmSubscription, requestBody, "application/json")
// 	if err != nil {
// 		problemDetail := "[Request Body] " + err.Error()
// 		rsp := models.ProblemDetails{
// 			Title:  "Malformed request syntax",
// 			Status: http.StatusBadRequest,
// 			Detail: problemDetail,
// 		}
// 		logger.DataRepoLog.Errorln(problemDetail)
// 		c.JSON(http.StatusBadRequest, rsp)
// 		return
// 	}
//
// 	req := httpwrapper.NewRequest(c.Request, sdmSubscription)
// 	req.Params["ueId"] = c.Params.ByName("ueId")
// 	req.Params["subsId"] = c.Params.ByName("subsId")
//
// 	rsp := producer.HandleUpdatesdmsubscriptions(req)
//
// 	responseBody, err := openapi.Serialize(rsp.Body, "application/json")
// 	if err != nil {
// 		logger.DataRepoLog.Errorln(err)
// 		problemDetails := models.ProblemDetails{
// 			Status: http.StatusInternalServerError,
// 			Cause:  "SYSTEM_FAILURE",
// 			Detail: err.Error(),
// 		}
// 		c.JSON(http.StatusInternalServerError, problemDetails)
// 	} else {
// 		c.Data(rsp.Status, "application/json", responseBody)
// 	}
// }
