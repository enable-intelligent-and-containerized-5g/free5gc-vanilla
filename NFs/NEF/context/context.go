package context

import (
	"fmt"
	"os"

	"github.com/google/uuid"

	"github.com/free5gc/openapi/Nnrf_NFDiscovery"
	"github.com/free5gc/openapi/Nnrf_NFManagement"
	"github.com/free5gc/openapi/Nudm_SubscriberDataManagement"
	"github.com/free5gc/openapi/models"
	"nef.com/factory"
	"nef.com/logger"
)

func init() {
	nefContext.NfInstanceID = uuid.New().String()
}

var nefContext NEFContext

type NEFContext struct {
	Name            string
	URIScheme       models.UriScheme
	UriScheme       models.UriScheme
	BindingIPv4     string
	RegisterIPv4    string
	SBIPort         int
	HttpIPv6Address string
	NfInstanceID    string
	NfId            string
	// Key    string
	// PEM    string
	// KeyLog string

	NrfUri string

	// Now only "IPv4" supported
	// TODO: support "IPv6", "IPv4v6", "Ethernet"
	SupportedPDUSessionType string

	//*** For ULCL ** //
	// ULCLSupport    bool
	// ULCLGroups     map[string][]string
	// LocalSEIDCount uint64

	NFManagementClient             *Nnrf_NFManagement.APIClient
	NFDiscoveryClient              *Nnrf_NFDiscovery.APIClient
	SubscriberDataManagementClient *Nudm_SubscriberDataManagement.APIClient
}

// RetrieveDnnInformation gets the corresponding dnn info from S-NSSAI and DNN

// func AllocateLocalSEID() uint64 {
// 	atomic.AddUint64(&nefContext.LocalSEIDCount, 1)
// 	return nefContext.LocalSEIDCount //if error delete this
// }

func InitNefContext(config *factory.Config) {
	if config == nil {
		logger.CtxLog.Error("Config is nil")
		return
	}

	logger.CtxLog.Infof("nefconfig Info: Version[%s] Description[%s]", config.Info.Version, config.Info.Description)
	configuration := config.Configuration
	if configuration.NefName != "" {
		nefContext.Name = configuration.NefName
	}

	sbi := configuration.Sbi
	if sbi == nil {
		logger.CtxLog.Errorln("Configuration needs \"sbi\" value")
		return
	} else {
		nefContext.URIScheme = models.UriScheme(sbi.Scheme)
		nefContext.RegisterIPv4 = factory.NEF_DEFAULT_IPV4 // default localhost
		nefContext.SBIPort = factory.NEF_DEFAULT_PORT_INT  // default port
		if sbi.RegisterIPv4 != "" {
			nefContext.RegisterIPv4 = sbi.RegisterIPv4
		}
		if sbi.Port != 0 {
			nefContext.SBIPort = sbi.Port
		}

		nefContext.BindingIPv4 = os.Getenv(sbi.BindingIPv4)
		if nefContext.BindingIPv4 != "" {
			logger.CtxLog.Info("Parsing ServerIPv4 address from ENV Variable.")
		} else {
			nefContext.BindingIPv4 = sbi.BindingIPv4
			if nefContext.BindingIPv4 == "" {
				logger.CtxLog.Warn("Error parsing ServerIPv4 address as string. Using the 0.0.0.0 address as default.")
				nefContext.BindingIPv4 = "0.0.0.0"
			}
		}
	}

	if configuration.NrfUri != "" {
		nefContext.NrfUri = configuration.NrfUri
	} else {
		logger.CtxLog.Warn("NRF Uri is empty! Using localhost as NRF IPv4 address.")
		nefContext.NrfUri = fmt.Sprintf("%s://%s:%d", nefContext.URIScheme, "127.0.0.1", 29510)
	}

	//SetupNFProfile(config)
}

func NEF_Self() *NEFContext {
	return &nefContext
}
