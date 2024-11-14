const DATA_API_URL = "https://data.api.trade.gov.uk/v1/"
const DATASET = "orp-regulations"
const VERSION = "v1.0.1" // latest causes a redirect which adds latency
const FORMAT = "json"
// export const S3_QUERY = buildQuery(filters)
// export const ENCODED_S3_QUERY = encodeURI(S3_QUERY)

export const DATASET_OBJECT_NAME = "uk_regulatory_documents"
export const URL = `${DATA_API_URL}datasets/${DATASET}/versions/${VERSION}/data?format=${FORMAT}`

// These should come from the API/Django backend, but for now they are hardcoded
export const DOCUMENT_TYPES = [
  {
    name: "Legislation",
    label: "Legislation",
  },
  {
    name: "Guidance",
    label: "Guidance",
  },
  {
    name: "Standards",
    label: "Standards",
  },
]

export const PUBLISHERS = [
  {
    name: "healthandsafetyexecutive",
    label: "Health and Safety Executive",
  },
  {
    name: "civilaviationauthority",
    label: "Civil Aviation Authority",
  },
  {
    name: "environmentagency",
    label: "Environment Agency",
  },
  {
    name: "defra",
    label: "Defra",
  },
  {
    name: "officeofgasandelectricitymarkets",
    label: "Office of Gas and Electricity Markets",
  },
  {
    name: "officeofrailandroad",
    label: "Office of Rail and Road",
  },
  {
    name: "naturalengland",
    label: "Natural England",
  },
  {
    name: "historicengland",
    label: "Historic England",
  },
  {
    name: "nationalhighways",
    label: "National Highways",
  },
  {
    name: "homesengland",
    label: "Homes England",
  },
  {
    name: "departmentfortransport",
    label: "Department for Transport",
  },
]
