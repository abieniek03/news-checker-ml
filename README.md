# News checker
REST API service to verify whether news is true or fake, working in AWS Cloud.

Dataset - <a href="https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets" rel="noopener noreferer" target="_blank">LINK</a>

## 🛠️ Used tools
<ul>
  <li>S3</li>
  <li>AWS Glue</li>
  <li>Athena</li>
  <li>SageMaker AI</li>
  <li>Lambda Functions</li>
  <li>API Gateway</li>
</ul>

## REST API - DOCS

### POST /news/check


#### Example request body
```JSON
  {
    "title": "Breaking News",
    "text": "This is a real news"
  }
```

#### Responses
| Code | Description                       |
| :-------- | :-------------------------------- |
| 200      | Success |
| 400      | Request body validation failed |
| 500      | Internal server error |
| 502      | Model error |

#### Success response example
```JSON
  {
    "data": {
      "label": "fake-news",
      "prob": 1.0000100135803223
    }
}
```

<hr>

#### Author - [Adrian Bieniek](https://github.com/abieniek03)
