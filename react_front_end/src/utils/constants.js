const DRF_API_URL = "http://localhost:8081/api/v1"
export const SEARCH_URL = `${DRF_API_URL}/search`
// export const PUBLISHERS_URL = `${DRF_API_URL}/retrieve/publishers/`

// These should come from the API/Django backend, but for now they are hardcoded
export const DOCUMENT_TYPES = [
  {
    name: "legislation",
    label: "Legislation",
  },
  {
    name: "guidance",
    label: "Guidance",
  },
  {
    name: "standard",
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
